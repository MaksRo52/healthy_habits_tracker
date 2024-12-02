from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (
    DurationValidator,
    PleasantHabitValidator,
    RelatedHabitValidator,
    RewardValidator,
    TimerValidator,
)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"

    validators = [
        RewardValidator(field="reward", field2="related_habit"),
        RelatedHabitValidator(field="related_habit"),
        DurationValidator(field="duration"),
        PleasantHabitValidator(field="is_nice_habit"),
        TimerValidator(field1="frequency_number", field2="frequency_unit"),
    ]
