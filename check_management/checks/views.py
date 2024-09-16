# checks/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Check

class CheckListView(ListView):
    model = Check
    template_name = 'checks/check_list.html'
    context_object_name = 'checks'

class CheckDetailView(DetailView):
    model = Check
    template_name = 'checks/check_detail.html'
    context_object_name = 'check'

class CheckCreateView(CreateView):
    model = Check
    template_name = 'checks/check_form.html'
    fields = ['check_number', 'amount', 'status', 'issue_date', 'client']
    success_url = reverse_lazy('check_list')

class CheckUpdateView(UpdateView):
    model = Check
    template_name = 'checks/check_form.html'
    fields = ['check_number', 'amount', 'status', 'issue_date', 'client']
    success_url = reverse_lazy('check_list')

class CheckDeleteView(DeleteView):
    model = Check
    template_name = 'checks/check_confirm_delete.html'
    success_url = reverse_lazy('check_list')