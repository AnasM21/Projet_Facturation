# clients/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Client

class ClientListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'

class ClientCreateView(CreateView):
    model = Client
    template_name = 'clients/client_form.html'
    fields = ['name', 'email', 'address']
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'clients/client_form.html'
    fields = ['name', 'email', 'address']
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')
