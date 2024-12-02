from datetime import timedelta

from rest_framework.serializers import ValidationError


class RewardValidator:
    """Исключает одновременный выбор связанной привычки и указания вознаграждения."""

    def __init__(self, field, field2):
        self.field = field
        self.field2 = field2

    def __call__(self, value):
        temp_value = dict(value).get(self.field)
        temp_value2 = dict(value).get(self.field2)
        if temp_value and temp_value2:
            raise ValidationError(
                "Поля связанной привычки и вознаграждения не могут быть заполнены одновременно."
            )


class DurationValidator:
    """Время выполнения должно быть не больше 120 секунд."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        temp_value = dict(value).get(self.field)
        if temp_value is not None and temp_value > timedelta(seconds=120):
            raise ValidationError("Время выполнения должно быть не больше 2 минут.")


class RelatedHabitValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        temp_value = dict(value).get(self.field)
        if temp_value:
            if not temp_value.is_nice_habit:
                raise ValidationError("Поле заполнено не верно")


class PleasantHabitValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        temp_value = dict(value).get(self.field)
        if temp_value:
            tmp_dict = dict(value)
            if (
                tmp_dict.get("reward") is not None
                or tmp_dict.get("related_habit") is not None
            ):
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения или связанной привычки"
                )


class TimerValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        frequency_in_days = 0
        num = dict(value).get(self.field1)
        unit = dict(value).get(self.field2)

        if num:
            if unit == "minutes":
                frequency_in_days = num / (60 * 24)
            elif unit == "hours":
                frequency_in_days = num / 24
            elif unit == "days":
                frequency_in_days = num

        if frequency_in_days > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")
