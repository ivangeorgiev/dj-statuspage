from django.urls import path
from . import views

app_name = 'djangostatuspage'

urlpatterns = [
  path('issues/', views.IssueList.as_view(), name='issues-list'),
  path('issues/<int:pk>/', views.IssueRetrieveUpdate.as_view(), name='issue'),
  path('status-pages/', views.StatusPageList.as_view(), name='status-pages-list'),
  path('status-pages/<str:pk>/', views.StatusPageView.as_view(), name='status-page'),
  path('systems/', views.SystemList.as_view(), name='systems-list'),
  path('ui/status-pages/<str:pk>/', views.view_status_page_ui, name='view_status_page_ui'),
]
