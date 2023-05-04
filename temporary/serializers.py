from rest_framework import serializers

from .models import Temporary


class TemporarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporary
        fields = ['id', 'day', 'shift_type', 'custom_time', 'night']


class TemporaryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporary
        fields = ['id', 'day', 'shift_type', 'night', 'custom_time']

    def validate_custom_time(self, value):
        shift_choices = Temporary.SHIFT_CHOICES

        if self.initial_data.get('shift_type') in [choice[0] for choice in shift_choices if
                                                   choice[0] != 'other'] and value:
            raise serializers.ValidationError("This field is not required.")
        if self.initial_data.get('shift_type') == 'other' and not value:
            raise serializers.ValidationError("This field is required.")
        return value

    def to_representation(self, instance):
        shift_choices = Temporary.SHIFT_CHOICES

        if instance.shift_type in [choice[0] for choice in shift_choices if choice[0] != 'other']:
            self.fields['custom_time'].read_only = True
        return super().to_representation(instance)
