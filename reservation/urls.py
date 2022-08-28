from rest_framework.routers import DefaultRouter
from .views import ReservationViewSet

router = DefaultRouter()
router.register('reservations', ReservationViewSet, basename='Reservations')

# Exporting urls to core.api.v1.urls to be recolected
urls = router.urls