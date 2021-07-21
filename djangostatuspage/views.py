from django.shortcuts import render, reverse
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Issue, StatusPage, System
from .serializers import IssueSerializer, StatusPageSerializer, SystemSerializer
from . import conf

class IssueList(generics.ListCreateAPIView):
  queryset = Issue.objects.all()
  serializer_class = IssueSerializer
  # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  # def perform_create(self, serializer):
  #   serializer.save(poster=self.request.user)

class IssueRetrieveUpdate(generics.RetrieveUpdateAPIView):
  queryset = Issue.objects.all()
  serializer_class = IssueSerializer


class SystemList(generics.ListAPIView):
  queryset = System.objects.all()
  serializer_class = SystemSerializer

class StatusPageList(generics.ListAPIView):
  queryset = StatusPage.objects.all()
  serializer_class = StatusPageSerializer

class StatusPageView(generics.RetrieveAPIView):
  queryset = StatusPage.objects.all()
  serializer_class = StatusPageSerializer


def view_status_page_ui(request, pk):
  current_namespace = request.resolver_match.namespace
  context = {
    'url_get_current_status_page':  reverse(f'{current_namespace}:status-page', kwargs={'pk':pk}),
    'status_page_id': pk,
    'auto_refresh_interval': 300000,
  }
  return render(request, conf.ui_template, context)
