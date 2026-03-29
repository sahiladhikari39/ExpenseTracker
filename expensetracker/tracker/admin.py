from django.contrib import admin
from tracker.models import *
# Register your models here.

admin.site.site_header = "Sahil"
admin.site.site_title = "Expense Tracker"
admin.site.site_url = "Expense Tracker"


admin.site.register(CurrentBalance)


@admin.action(description="Make it Debit")
def make_debit(ModelAdmin, request, queryset):
    for q in queryset:
        obj = TrackingHistory.objects.get(id = q.id)
        if obj.amount > 0 :
            obj.amount *= -1
            obj.save()
    queryset.update(expense_type = 'DEBIT')
        



class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "current_balance",
        "amount",
        "description",
        "expense_type",
        "created_at",
        "status"
    ]
    actions = [make_debit]

    def status(self, obj):
        type = "Green" if obj.amount>0 else "Red"
        return type

    search_fields = ["expense_type"]

admin.site.register(TrackingHistory, TrackingHistoryAdmin)