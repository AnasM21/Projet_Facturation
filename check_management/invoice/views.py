# invoice/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Invoice

class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice/invoice_list.html'  # Ensure this path is correct
    context_object_name = 'invoices'

class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoice/invoice_detail.html'  # Ensure this path is correct
    context_object_name = 'invoice'

class InvoiceCreateView(CreateView):
    model = Invoice
    template_name = 'invoice/invoice_form.html'  # Ensure this path is correct
    fields = ['invoice_number', 'client', 'amount', 'status', 'issue_date', 'due_date', 'paid_by_check']
    success_url = reverse_lazy('invoice_list')

class InvoiceUpdateView(UpdateView):
    model = Invoice
    template_name = 'invoice/invoice_form.html'  # Ensure this path is correct
    fields = ['invoice_number', 'client', 'amount', 'status', 'issue_date', 'due_date', 'paid_by_check']
    success_url = reverse_lazy('invoice_list')

class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoice/invoice_confirm_delete.html'  # Ensure this path is correct
    success_url = reverse_lazy('invoice_list')
