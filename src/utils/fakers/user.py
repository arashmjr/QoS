import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "accounts.User"

    password = "foo"
    set_password = factory.PostGenerationMethodCall("set_password", "foo")
    phone_number = factory.Faker("numerify", text="+%########!!!!!!")
