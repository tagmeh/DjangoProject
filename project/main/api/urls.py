from rest_framework import routers

from main.api.view import PlayerViewSet

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)