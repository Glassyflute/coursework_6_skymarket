from django.urls import include, path

from rest_framework.routers import SimpleRouter


# настройка роутов для модели Comment
from ads.views import CommentViewSet

comments_router = SimpleRouter()

# в роуте мы регистрируем ViewSet, который импортирован из приложения Djoser
comments_router.register("comments", CommentViewSet, basename="comments")


urlpatterns = [
    path("", include(comments_router.urls)),
]

