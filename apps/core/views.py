from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WebsiteSettings
from .serializers import WebsiteSettingsSerializer, WebsiteSettingsKeyValueSerializer

# Create your views here.


class WebsiteSettingsAPIView(APIView):
    """DRF API view to return website settings data"""

    def get(self, request, *args, **kwargs):
        """Return all website settings as JSON"""
        try:
            settings = WebsiteSettings.objects.all()

            # Use the key-value serializer for simple key-value response
            serializer = WebsiteSettingsKeyValueSerializer(settings)

            return Response(
                {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"success": False, "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class WebsiteSettingAPIView(APIView):
    """DRF API view to return a specific website setting by key"""

    def get(self, request, key, *args, **kwargs):
        """Return a specific website setting by key"""
        try:
            setting = WebsiteSettings.objects.get(key=key)
            serializer = WebsiteSettingsSerializer(setting)

            return Response(
                {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        except WebsiteSettings.DoesNotExist:
            return Response(
                {"success": False, "error": f'Setting with key "{key}" not found'},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"success": False, "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )