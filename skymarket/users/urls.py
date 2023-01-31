from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

from users.views import UserImageView

users_router = SimpleRouter()

# в роуте мы регистрируем ViewSet, который импортирован из приложения Djoser
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
    path("users/<int:pk>/upload_image/", UserImageView.as_view())
]




