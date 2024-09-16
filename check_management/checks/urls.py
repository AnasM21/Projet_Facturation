# checks/urls.py
from django.urls import path
from .views import CheckListView, CheckDetailView, CheckCreateView, CheckUpdateView, CheckDeleteView

urlpatterns = [
    path('', CheckListView.as_view(), name='check_list'),
    path('<int:pk>/', CheckDetailView.as_view(), name='check_detail'),
    path('create/', CheckCreateView.as_view(), name='check_create'),
    path('<int:pk>/update/', CheckUpdateView.as_view(), name='check_update'),
    path('<int:pk>/delete/', CheckDeleteView.as_view(), name='check_delete'),
]