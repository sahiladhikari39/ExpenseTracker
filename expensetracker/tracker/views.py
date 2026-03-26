from django.shortcuts import render, redirect
from .models import TrackingHistory, CurrentBalance
from django.db.models import Sum

# Create your views here.

def index(request):
    if request.method == "POST":
        description = request.POST.get('description')
        amount = request.POST.get('amount')

        current_balance, _ = CurrentBalance.objects.get_or_create(id=1) 

        expense_type = "CREDIT" if float(amount) > 0 else "DEBIT"

        tracking_history = TrackingHistory.objects.create(amount=amount, description=description, current_balance=current_balance, expense_type=expense_type)
        current_balance.current_balance += float(tracking_history.amount)
        current_balance.save()

        
        return redirect('/')
    
    income = 0
    expense = 0
    for data in TrackingHistory.objects.all():
        if data.expense_type == "CREDIT":
            income += data.amount
        else:
            expense += data.amount

    current_balance, _ = CurrentBalance.objects.get_or_create(id=1) 
    context = {"income": income, "expense": expense, "transactions": TrackingHistory.objects.all(), "current_balance": current_balance}
    return render(request, "tracker/index.html", context)


def delete_transaction(request, id):
    tracking_history = TrackingHistory.objects.filter(id=id)

    if tracking_history.exists():
        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
        tracking_history = tracking_history[0]

        current_balance.current_balance = current_balance.current_balance - tracking_history.amount
        current_balance.save()

    tracking_history.delete()
    return redirect('/')