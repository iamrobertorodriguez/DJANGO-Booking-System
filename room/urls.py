from rest_framework.routers import DefaultRouter
from .views import RoomViewSet

router = DefaultRouter()
router.register('rooms', RoomViewSet, basename='Rooms')

# Exporting urls to core.api.v1.urls to be recolected
urls = router.urls