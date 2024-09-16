from django.db import models
from clients.models import Client
from checks.models import Check

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='invoices')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Overdue', 'Overdue')])
    issue_date = models.DateField()
    due_date = models.DateField()
    paid_by_check = models.ForeignKey(Check, null=True, blank=True, on_delete=models.SET_NULL, related_name='invoices')

    class Meta:
        db_table = 'invoice'  # Custom table name
        
    
    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.client.name}"
