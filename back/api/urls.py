from django.urls import path

from api.api_views import (
    MainPage,
)

urlpatterns = [
    path(
        "welcome/",
        MainPage.as_view(),
        name='welcome'
    )
]
