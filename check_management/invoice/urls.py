# invoices/urls.py
from django.urls import path
from .views import InvoiceListView, InvoiceDetailView, InvoiceCreateView, InvoiceUpdateView, InvoiceDeleteView, generate_client_invoice_pdf
urlpatterns = [
    path('', InvoiceListView.as_view(), name='invoice_list'),
    path('<int:pk>/', InvoiceDetailView.as_view(), name='invoice_detail'),
    path('create/', InvoiceCreateView.as_view(), name='invoice_create'),
    path('<int:pk>/update/', InvoiceUpdateView.as_view(), name='invoice_update'),
    path('<int:pk>/delete/', InvoiceDeleteView.as_view(), name='invoice_delete'),
    path('client/<int:client_id>/invoices/pdf/', generate_client_invoice_pdf, name='generate_client_invoice_pdf'),
    
]