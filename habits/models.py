from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    FREQUENCY_UNITS = [
        ("minutes", "минуты"),
        ("hours", "часы"),
        ("days", "дни"),
    ]
    name = models.CharField(
        max_length=100, verbose_name="название привыяки", **NULLABLE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Cоздатель привычки",
        **NULLABLE,
    )
    place = models.CharField(max_length=75, verbose_name="место привычки")
    time = models.TimeField(verbose_name="время дня привычки")
    action = models.CharField(max_length=75, verbose_name="действие привычки")
    is_nice_habit = models.BooleanField(verbose_name="признак приятной привычки")
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Связанная привычка"
    )
    frequency_number = models.PositiveIntegerField(verbose_name="Количество раз")
    frequency_unit = models.CharField(
        max_length=10,
        choices=FREQUENCY_UNITS,
        default="days",
        verbose_name="Единицы измерения",
    )
    reward = models.CharField(max_length=200, verbose_name="Вознаграждение", **NULLABLE)
    duration = models.DurationField(verbose_name="Длительность действия")
    is_public = models.BooleanField(default=True, verbose_name="Публичная")

    def __str__(self):
        # Строковое отображение объекта
        return self.name

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
