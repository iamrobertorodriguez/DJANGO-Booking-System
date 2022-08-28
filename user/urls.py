from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, StaffViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet, basename='Clients')
router.register('staff', StaffViewSet, basename='Staff')

# Exporting urls to core.api.v1.urls to be recolected
urls = router.urls