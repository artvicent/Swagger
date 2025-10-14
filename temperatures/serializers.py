from rest_framework import serializers
from .models import CityTemperature

class CityTemperatureSerializer(serializers.ModelSerializer):
    city = serializers.CharField(help_text="Nombre de la ciudad (único).")
    temperature = serializers.DecimalField(max_digits=5, decimal_places=2, help_text="Temperatura en °C (decimal).")
    
    class Meta:
        model = CityTemperature
        fields = ['id', 'city', 'temperature', 'last_updated']
        read_only_fields = ['id', 'last_updated']

from drf_yasg import openapi

example_resp = openapi.Response(
    description="Ejemplo de respuesta",
    schema=CityTemperatureSerializer()
)
# luego en swagger_auto_schema responses={201: example_resp}

