from rest_framework import serializers

from main.models import Player


class PlayerCreateSerializer(serializers.ModelSerializer):
    """
    Only used for the create/post action
    Contains initial validations
    """

    def validate_age(self, age):
        """
        Implicit method from DRF. "validate_<field_name>"
        Validate the Player is old enough to be on a quest (>10) but young enough to survive the quest (<100)
        """
        if age < 10 or age > 100:  # Reasonable age for a quest!
            raise serializers.ValidationError('Age should be between 10 and 100.')
        return age

    class Meta:
        model = Player
        fields = (
            'id',
            'name',
            'favorite_color',
            'age'
        )


class PlayerViewSerializer(serializers.ModelSerializer):
    """ Used for both the list and retrieve viewset actions. """
    class Meta:
        model = Player
        fields = '__all__'

