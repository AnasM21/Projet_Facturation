# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # Import TemplateView for rendering home.html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
    path('checks/', include('checks.urls')),
    path('invoice/', include('invoice.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Home page route
]
