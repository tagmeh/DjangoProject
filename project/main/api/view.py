import random

from rest_framework.viewsets import ModelViewSet

from main import models
from main.api import serializers
from main.models import PlayerTypes


class PlayerViewSet(ModelViewSet):
    queryset = models.Player.objects.all()
    lookup_field = 'pk'
    serializer_classes = {
        'create': serializers.PlayerCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, serializers.PlayerViewSerializer)

    def perform_create(self, serializer):
        serializer.type = random.choice(PlayerTypes.choices)
        serializer.save()


class CompanionViewSet(ModelViewSet):
    queryset = models.Companion.objects.all()
    lookup_field = 'pk'
    serializer_class = serializers.CompanionSerializer