import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.accounts.models.user_manaer import UserManager


class User(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="{}\n{}".format(
            _("Phone number must be entered in the format: '+999999999'."),
            _("Up to 15 digits allowed."),
        ),
    )
    phone_number = models.CharField(
        verbose_name=_("phone number"),
        validators=[phone_regex],
        max_length=17,
        unique=True,
    )

    objects = UserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.phone_number}"
