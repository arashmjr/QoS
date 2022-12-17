import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Website(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=100, verbose_name=_("address"))
    delay = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.address
