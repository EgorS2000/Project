from rest_framework import serializers

from Project.models import UserInfo, Likes


class UserInfoSerializer(serializers.ModelSerializer):
    likes_count = serializers.ReadOnlyField(
        help_text="Likes count",
    )

    class Meta:
        model = UserInfo
        fields = ('name', 'last_name', 'age', 'photo', 'user_id', 'likes_count')
    # name = serializers.CharField(
    #     help_text="Name",
    # )
    # last_name = serializers.CharField(
    #     help_text="Last name",
    # )
    # age = serializers.IntegerField(
    #     help_text="Age",
    # )
    # photo = serializers.CharField(
    #     help_text="Photo",
    #     allow_null=True
    # )


class GiveLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'
