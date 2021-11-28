from django.urls import path

from api.api_views import (
    ShowMyProfile,
    UpdateMyProfile,
    GiveLike,
    HideMyLike
)

urlpatterns = [
    path(
        "my_profile/",
        ShowMyProfile.as_view(),
        name='my profile'
    ),
    path(
        "update_my_profile/",
        UpdateMyProfile.as_view(),
        name='update my profile'
    ),
    path(
        "give_like/",
        GiveLike.as_view(),
        name='give like'
    ),
    path(
        'hide_like/',
        HideMyLike.as_view(),
        name='hide my like'
    )
]
