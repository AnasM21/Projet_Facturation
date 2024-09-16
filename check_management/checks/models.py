from django.db import models
from clients.models import Client

class Check(models.Model):
    check_number = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Cleared', 'Cleared'), ('Bounced', 'Bounced')])
    issue_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='checks')

    class Meta:
        db_table = 'checks'  # Custom table name
        
    def __str__(self):
        return f"Check {self.check_number} - {self.client.name} - {self.status}"

    