from django.conf import settings

__version__ = '0.1.0'


class Config:
  DEFAULT_SETTINS = {
    'UI_TEMPLATE': 'djangostatuspage/status_page.html',
  }

  def __init__(self):
    self.settings = getattr(settings, 'DJANGOSTATUSPAGE', self.DEFAULT_SETTINS)

  @property
  def ui_template(self):
    return self.get_setting('UI_TEMPLATE')
    
  def get_setting(self, setting_name):
    return self.settings.get(setting_name, self.DEFAULT_SETTINS[setting_name])


conf = Config()

