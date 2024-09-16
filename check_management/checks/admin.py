from django.contrib import admin
from .models import Check

@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ('check_number', 'amount', 'status', 'issue_date', 'client')
    search_fields = ('check_number', 'client__name')
    list_filter = ('status', 'issue_date', 'client')
