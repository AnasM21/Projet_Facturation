from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Invoice, Client
from fpdf import FPDF

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

    def get_context_data(self, **kwargs):
        # Add clients to the context
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        return context

class InvoiceUpdateView(UpdateView):
    model = Invoice
    template_name = 'invoice/invoice_form.html'  # Ensure this path is correct
    fields = ['invoice_number', 'client', 'amount', 'status', 'issue_date', 'due_date', 'paid_by_check']
    success_url = reverse_lazy('invoice_list')

    def get_context_data(self, **kwargs):
        # Add clients to the context
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        return context

class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoice/invoice_confirm_delete.html'  # Ensure this path is correct
    success_url = reverse_lazy('invoice_list')

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 0, 0)
        self.set_fill_color(0, 102, 204)
        self.cell(0, 10, 'Invoice for {}'.format(self.client_name), 0, 1, 'C')
        self.ln(10)

    def client_details(self, client):
        self.set_font('Arial', '', 10)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, 'Client Details:', 0, 1)
        self.cell(0, 10, f'Email: {client.email}', 0, 1)
        self.cell(0, 10, f'Name: {client.name}', 0, 1)
        self.cell(0, 10, f'Address: {client.address}', 0, 1)
        self.ln(10)

    def invoice_table(self, invoices):
        self.set_font('Arial', 'B', 10)
        self.set_fill_color(230, 230, 230)
        self.cell(50, 10, 'Invoice Number', 1, 0, 'C', fill=True)
        self.cell(50, 10, 'Amount', 1, 0, 'C', fill=True)
        self.cell(50, 10, 'Status', 1, 0, 'C', fill=True)
        self.cell(40, 10, 'Issue Date', 1, 1, 'C', fill=True)

        self.set_font('Arial', '', 10)
        fill = False
        total_amount = 0
        for invoice in invoices:
            self.set_fill_color(245, 245, 245) if fill else self.set_fill_color(255, 255, 255)
            self.cell(50, 10, invoice.invoice_number, 1, 0, 'C', fill=True)
            self.cell(50, 10, f"{invoice.amount:.2f} DH", 1, 0, 'C', fill=True)
            self.cell(50, 10, invoice.status, 1, 0, 'C', fill=True)
            self.cell(40, 10, invoice.issue_date.strftime('%b %d, %Y'), 1, 1, 'C', fill=True)
            fill = not fill
            total_amount += invoice.amount

        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 102, 204)
        self.cell(0, 10, f'Total Amount: {total_amount:.2f} DH', 0, 1, 'R')

def generate_client_invoice_pdf(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    invoices = Invoice.objects.filter(client=client)

    pdf = PDF()
    pdf.client_name = client.name
    pdf.add_page()

    pdf.client_details(client)
    pdf.invoice_table(invoices)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{client.name}_invoices.pdf"'
    response.write(pdf.output(dest='S').encode('latin1'))

    return response
