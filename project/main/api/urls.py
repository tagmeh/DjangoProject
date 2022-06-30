from rest_framework import routers

from main.api import view

router = routers.DefaultRouter()
router.register(r'players', view.PlayerViewSet)
router.register(r'companions', view.CompanionViewSet)
