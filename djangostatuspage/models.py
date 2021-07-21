from django.db import models

class System(models.Model):
  system_id = models.CharField(max_length=255, primary_key=True)
  parent_system = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="subsystems")
  parent_system_id_path = models.CharField(max_length=2048, blank=True, null=True)
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  rank = models.IntegerField(default=0)

  class Meta:
    ordering = ('rank', 'name', 'system_id', )
    indexes = [
      models.Index(fields=['system_id']),
      models.Index(fields=['parent_system_id_path']),
    ]

  def __str__(self):
    return f'{self.name}'


class Issue(models.Model):

  ENUM_SEVERITY = (
    ('Outage', 'Major outage'),
    ('Degraded', 'Degraded performance'),
    ('Minor', 'Minor'),
  )

  ENUM_STATUS = (
    ('New', 'New'),
    ('Investigation', 'Under Investigation'),
    ('Resolved', 'Resolved'),
    ('Closed', 'Closed'),
  )
  RESOLVED_STATUSES = ['Closed', 'Resolved']

  issue_id = models.BigAutoField(primary_key=True)
  original_issue_id = models.CharField(max_length=255)
  system = models.ForeignKey(System, on_delete=models.CASCADE, related_name='issues')
  title = models.CharField(max_length=255)
  severity = models.CharField(max_length=32, choices=ENUM_SEVERITY, blank=True, null=True)
  description = models.TextField(blank=True)
  status = models.CharField(max_length=64, choices=ENUM_STATUS, default='N')
  is_resolved = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  resolved_at = models.DateTimeField(default=None, null=True, blank=True)

  class Meta:
    indexes = [
      models.Index(fields=['original_issue_id'])
    ]

  def __str__(self):
    return f'{self.issue_id}: {self.title} ({self.severity_label(self.severity)}, { dict(self.ENUM_STATUS)[self.status]})'

  @classmethod
  def severity_label(cls, severity):
    return dict(cls.ENUM_SEVERITY)[severity]

class StatusPage(models.Model):
  status_page_id = models.CharField(max_length=255, primary_key=True)
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  systems = models.ManyToManyField('System', related_name='status_papges', blank=True)

  class Meta:
    ordering = ('name',)
 
  def __str__(self):
    return f'{self.name}'
