import factory
from src.apps.reminders.models import Reminder
from src.utils.fakers.user import UserFactory


class ReminderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reminder

    user = factory.SubFactory(UserFactory)
    title = factory.Faker("name")
    reminder_time = factory.Faker("date_time")
    threshold = factory.Faker("date_time")
