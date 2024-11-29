from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = PhoneNumberField(
        null=True, blank=True, verbose_name="Номер телефона"
    )
    country = models.CharField(
        max_length=50, verbose_name="Страна", null=True, blank=True
    )
    photo = models.ImageField(
        upload_to="users/photos/",
        verbose_name="Фото",
        help_text="Загрузите своё фото.",
        null=True,
        blank=True,
    )
    token = models.CharField(
        max_length=100, verbose_name="Токен", null=True, blank=True
    )
    tg_chat_id = models.CharField(
        max_length=50, verbose_name="Телеграм chat-id", null=True, blank=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
