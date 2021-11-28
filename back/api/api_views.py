import sys
from datetime import date, datetime

from rest_framework import status
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.shortcuts import get_list_or_404, get_object_or_404
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from Project.models import UserInfo, Likes

from ProjectDjangoREST.env_settings import MAX_FILE_SIZE_IN_BYTES
from api.serializers import UserInfoSerializer, GiveLikeSerializer

from common.utils import serialization


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        operation_id="Show profile info.",
        operation_description="Show profile info."
    )
)
class ShowMyProfile(ListAPIView):
    serializer_class = UserInfoSerializer
    permissions = [IsAuthenticated]

    def get_queryset(self):
        info = get_list_or_404(UserInfo.objects.filter(
            user_id=self.request.user.id
        ).all())
        # data = serialization(
        #     serializer=self.serializer_class,
        #     data=info,
        #     mode='get'
        # )
        # return Response(data=info, status=status.HTTP_200_OK)
        # return {'data': info}
        return info
        # likes_count = Likes.objects.filter(who_take=self.request.user.id).all().count() or 0

        # data = {
        #     "name": info.name,
        #     "last_name": info.last_name,
        #     "age": info.age,
        #     "photo": info.photo,
        #     "user": info.user,
        #     "likes_count": likes_count
        # }

        # data = serialization(
        #     serializer=self.serializer_class,
        #     data=data,
        #     mode='get'
        # )
        # print(data)
        # return data
        # return None


@method_decorator(
    name='update',
    decorator=swagger_auto_schema(
        operation_id="Update profile info.",
        operation_description="Update profile info."
    )
)
class UpdateMyProfile(UpdateAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        if request.data is None:
            return Response(
                data='Info is empty',
                status=status.HTTP_400_BAD_REQUEST
            )
        name, last_name, age, file_name = None, None, None, None
        if 'name' in request.data:
            name = request.data.get('name')
        if 'last_name' in request.data:
            last_name = request.data.get('last_name')
        if 'age' in request.data:
            age = request.data.get('age')
        if 'file' in request.data:
            file = request.FILES.get('file')
            file_size = sys.getsizeof(file)
            if file_size > MAX_FILE_SIZE_IN_BYTES:
                return Response(
                    data={'message': "File size can't be larger then 20 MB"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            file_name = default_storage.save(
                f'homeworks/{str(date.today().strftime("%d-%m-%Y"))}/'
                f'{str(datetime.now().strftime("%H-%M-%S"))}/{file.name}',
                file
            )

        info = get_object_or_404(
            UserInfo,
            user_id=self.request.user.id
        )

        data = {
            'name': name or info.name,
            'last_name': last_name or info.last_name,
            'age': age or info.age,
            'photo': f'/media/{file_name}' if file_name else info.photo
        }

        serializer = serialization(
            serializer=self.serializer_class,
            data=data,
            mode='update',
            instance=info
        )

        return Response(data={
            'data': serializer.data
        },
            status=status.HTTP_200_OK
        )


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        operation_id="Give like to another user.",
        operation_description="Give like to another user."
    )
)
class GiveLike(CreateAPIView):
    serializer_class = GiveLikeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        to = request.data.get('user_id')
        _from = request.user.id

        data = {
            'who_give': _from,
            'who_take': to,
            'hidden': False
        }

        serialization(
            serializer=self.serializer_class,
            data=data,
            mode='create'
        )

        return Response(data={
            'data': 'Like has been given'
        },
            status=status.HTTP_201_CREATED
        )


@method_decorator(
    name='put',
    decorator=swagger_auto_schema(
        operation_id="Hide like.",
        operation_description="Hide like."
    )
)
class HideMyLike(UpdateAPIView):
    serializer_class = GiveLikeSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        like_id = request.data['like_id']

        like = get_object_or_404(
            Likes,
            id=like_id
        )

        serializer = serialization(
            serializer=self.serializer_class,
            data={'hidden': True},
            mode='update',
            instance=like
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
