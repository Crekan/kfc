from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Temporary


class TemporarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporary
        fields = ['id', 'day', 'shift_type', 'custom_time', 'night']


class TemporaryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporary
        fields = ['id', 'day', 'shift_type', 'night', 'custom_time']
        validators = [
            UniqueTogetherValidator(
                queryset=Temporary.objects.all(),
                fields=['day'],
                message='День уже существует'
            )
        ]

    def validate_custom_time(self, value):
        shift_choices = Temporary.SHIFT_CHOICES

        if self.initial_data.get('shift_type') in [choice[0] for choice in shift_choices if
                                                   choice[0] != 'Другое'] and value:
            raise serializers.ValidationError('Это поле должно заполнся при выборе "Другое".')
        if self.initial_data.get('shift_type') == 'Другое' and not value:
            raise serializers.ValidationError('Это поле должно заполнся при выборе "Другое".')
        return value

    def to_representation(self, instance):
        shift_choices = Temporary.SHIFT_CHOICES

        if instance.shift_type in [choice[0] for choice in shift_choices if choice[0] != 'Другое']:
            self.fields['custom_time'].read_only = True
        return super().to_representation(instance)
