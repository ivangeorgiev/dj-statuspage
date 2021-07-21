from rest_framework import serializers
from django.db.models import Count, F
from collections import defaultdict
from .models import (
  Issue,
  StatusPage,
  System,
)
import typing

__all__ = ('IssueSerializer')

class IssueSerializer(serializers.ModelSerializer):
  is_resolved = serializers.ReadOnlyField()

  class Meta:
    
    model = Issue
    fields = ('issue_id', 'original_issue_id', 'system', 'title', 'severity', 'description', 'status', 'is_resolved')

class SystemSerializer(serializers.ModelSerializer):
  parent_system_id = serializers.ReadOnlyField(source='parent_system.id')

  class Meta:
    model = System
    fields = ('system_id', 'parent_system_id', 'name', 'description')

class OpenIssuesField(serializers.DictField):
  child = serializers.CharField()

class StatusPageSerializer(serializers.ModelSerializer):
  open_issues = serializers.SerializerMethodField()
  systems = serializers.SerializerMethodField()

  class Meta:
    model = StatusPage
    fields = ('status_page_id', 'name', 'description', 'systems', 'open_issues')
    
  def get_open_issues(self, status_page):
    return {}

  def get_systems(self, status_page):
    def get_system_record(system):
      issues = system.issues.all()
      open_issues = issues.filter(is_resolved=False)
      tag_counts = open_issues.values().annotate(count=Count('severity'))
      subsystem_tag_counts = defaultdict(lambda : {'count':0, 'label': ''})
      for c in tag_counts:
        subsystem_tag_counts[c['severity']] = {
          'count': c['count'],
          'label': Issue.severity_label(c['severity']),
          }
      subsystem_issue_count = 0
      for subsystem in system.subsystems.all():
        sysbsystem_record = get_system_record(subsystem)
        for severity, item in sysbsystem_record['open_issues']['by_severity'].items():
          count = item['count']
          subsystem_tag_counts[severity]['count'] += count
          subsystem_tag_counts[severity]['label'] = item['label']
          subsystem_issue_count += count
      system_record = {
        'id': system.system_id,
        'parent_id': system.parent_system.system_id if system.parent_system else None,
        'name': system.name,
        'description': system.description,
        'open_issues': {
          'count': open_issues.count(),
          'by_severity': {t['severity']:{'count':t['count'], 'label':Issue.severity_label(t['severity'])} for t in tag_counts},
          'with_subsystems': {
            'count': subsystem_issue_count,
            'by_severity': subsystem_tag_counts,
          }
        }
      }
      return system_record

    result = []
    for system in status_page.systems.all():
      system_record = get_system_record(system)
      result.append(system_record)
    return result