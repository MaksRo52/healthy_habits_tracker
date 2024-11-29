from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="test1@example.com")
        user.set_password("test")
        user.is_staff = False
        user.is_superuser = False
        user.is_active = True
        user.save()
        user = User.objects.create(email="test2@example.com")
        user.set_password("test")
        user.is_staff = False
        user.is_superuser = False
        user.is_active = True
        user.save()
        user = User.objects.create(email="test3@example.com")
        user.set_password("test")
        user.is_staff = False
        user.is_superuser = False
        user.is_active = True
        user.save()
