from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import CityTemperature
from .serializers import CityTemperatureSerializer

class CityTemperatureViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar temperaturas de ciudades.
    GET (list/retrieve) es público.
    POST/PUT/DELETE requieren token.
    """
    queryset = CityTemperature.objects.all().order_by('city')
    serializer_class = CityTemperatureSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # --- Documentación / ejemplos ---
    city_param = openapi.Parameter(
        'city', openapi.IN_QUERY, description="Nombre de la ciudad para filtrar (opcional)", type=openapi.TYPE_STRING
    )

    example_create = {
        "city": "Madrid",
        "temperature": "23.50"
    }

    example_update = {
        "city": "Madrid",
        "temperature": "25.00"
    }

    @swagger_auto_schema(
        operation_description="Listar todas las temperaturas registradas.",
        manual_parameters=[city_param],
        responses={200: CityTemperatureSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        """
        Devuelve la lista de temperaturas.
        (docstring: explica el propósito del endpoint)
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crear un nuevo registro de temperatura. Requiere autenticación (Token).",
        request_body=CityTemperatureSerializer,
        responses={201: CityTemperatureSerializer, 400: 'Bad Request'},
        examples={'application/json': example_create}
    )
    def create(self, request, *args, **kwargs):
        """Crear un registro nuevo con city y temperature."""
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener detalle de una temperatura por ID.",
        responses={200: CityTemperatureSerializer, 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        """Obtiene un registro por su id."""
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar completamente un registro existente (PUT). Requiere autenticación (Token).",
        request_body=CityTemperatureSerializer,
        responses={200: CityTemperatureSerializer, 400: 'Bad Request', 404: 'Not Found'},
        examples={'application/json': example_update}
    )
    def update(self, request, *args, **kwargs):
        """Actualiza city y temperature del registro indicado por id."""
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Eliminar un registro por ID. Requiere autenticación (Token).",
        responses={204: 'No Content', 404: 'Not Found'}
    )
    def destroy(self, request, *args, **kwargs):
        """Elimina el registro indicado por id."""
        return super().destroy(request, *args, **kwargs)

