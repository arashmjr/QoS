from datetime import timedelta

import factory
from django.utils import timezone
from src.apps.reminders.models import Reminder
from src.utils.fakers.user import UserFactory


class ReminderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reminder

    user = factory.SubFactory(UserFactory)
    title = factory.Faker("name")
    reminder_time = timezone.now() + timedelta(days=5)
    threshold = timezone.now() + timedelta(days=3)
