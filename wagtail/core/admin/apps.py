from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

from . import checks  # NOQA


class WagtailAdminAppConfig(AppConfig):
    name = 'wagtail.core.admin'
    label = 'wagtailadmin'
    verbose_name = _("Wagtail admin")
    default_auto_field = 'django.db.models.AutoField'
