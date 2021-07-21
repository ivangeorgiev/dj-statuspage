from .models import Issue, System
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime

@receiver(pre_save, sender=Issue)
def pre_save_issue(sender, instance:Issue, raw:bool, *args, **kwargs):
  if raw:
    return
  if instance.status in Issue.RESOLVED_STATUSES:
    instance.is_resolved = True
  else:
    instance.is_resolved = False

  if instance.is_resolved:
    if instance.resolved_at is None:
      instance.resolved_at = datetime.utcnow()
  else:
    instance.resolved_at = None

@receiver(pre_save, sender=System)
def pre_save_system(sender, instance:System, raw:bool, *args, **kwargs):
  if raw:
    return
  parent_system_id_path = '/'
  if instance.parent_system:
    parent_system_id_path = f'{instance.parent_system.parent_system_id_path}'
  instance.parent_system_id_path = f'{parent_system_id_path}{instance.rank}/{instance.system_id}/'
  
  for subsystem in instance.subsystems.all():
    subsystem.parent_system = instance
    subsystem.save()

