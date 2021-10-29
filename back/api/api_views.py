from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        operation_id="Show info.",
        operation_description="Show info."
    )
)
class MainPage(ListAPIView):
    permissions = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if not request.data['name'].strip():
            return Response(
                data='Name is empty',
                status=status.HTTP_400_BAD_REQUEST
            )
        result = f"Welcome, {request.data['name']}"

        return Response(data=result, status=status.HTTP_200_OK)
