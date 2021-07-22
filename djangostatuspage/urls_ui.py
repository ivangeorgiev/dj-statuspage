from django.urls import path
from . import views

app_name = 'djangostatuspage-ui'

urlpatterns = [
  path('status-pages/<str:pk>/', views.view_status_page_ui, name='view_status_page_ui'),
]
