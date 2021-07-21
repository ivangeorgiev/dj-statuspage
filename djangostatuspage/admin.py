from django.contrib import admin
from .models import Issue, StatusPage, System

class SystemAdmin(admin.ModelAdmin):
    list_display = ('rank', 'system_id', 'parent_system', 'name')
    search_fields = ['system_id', 'name']

class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_id', 'system', 'original_issue_id', 'severity', 'status', 'title')
    # search_fields = ['system_id', 'name']


admin.site.register(Issue, IssueAdmin)
admin.site.register(StatusPage)
admin.site.register(System, SystemAdmin)
