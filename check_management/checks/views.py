from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Check, Client

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

    def get_context_data(self, **kwargs):
        # Add clients to the context
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        return context

class CheckUpdateView(UpdateView):
    model = Check
    template_name = 'checks/check_form.html'
    fields = ['check_number', 'amount', 'status', 'issue_date', 'client']
    success_url = reverse_lazy('check_list')

    def get_context_data(self, **kwargs):
        # Add clients to the context
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        return context

class CheckDeleteView(DeleteView):
    model = Check
    template_name = 'checks/check_confirm_delete.html'
    success_url = reverse_lazy('check_list')
