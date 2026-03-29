from django.db import models

# Create your models here.
class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0)

    def __str__(self):
        return str(self.current_balance)


class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.CharField(max_length=100)
    expense_type = models.CharField(choices=(('CREDIT', 'CREDIT'), ('DEBIT', 'DEBIT')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"The amount for '{self.description}' is ${self.amount} and the type id {self.expense_type}"