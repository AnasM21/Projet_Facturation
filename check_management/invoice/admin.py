from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'client', 'amount', 'status', 'issue_date', 'due_date', 'paid_by_check')
    search_fields = ('invoice_number', 'client__name')
    list_filter = ('status', 'issue_date', 'due_date')
