from rest_framework.routers import DefaultRouter
from .views import CityTemperatureViewSet

router = DefaultRouter()
router.register(r'temperatures', CityTemperatureViewSet, basename='citytemperature')

urlpatterns = router.urls
