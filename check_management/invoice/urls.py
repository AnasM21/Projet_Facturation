# invoices/urls.py
from django.urls import path
from .views import InvoiceListView, InvoiceDetailView, InvoiceCreateView, InvoiceUpdateView, InvoiceDeleteView

urlpatterns = [
    path('', InvoiceListView.as_view(), name='invoice_list'),
    path('<int:pk>/', InvoiceDetailView.as_view(), name='invoice_detail'),
    path('create/', InvoiceCreateView.as_view(), name='invoice_create'),
    path('<int:pk>/update/', InvoiceUpdateView.as_view(), name='invoice_update'),
    path('<int:pk>/delete/', InvoiceDeleteView.as_view(), name='invoice_delete'),
]