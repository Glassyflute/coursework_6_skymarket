from django.urls import include, path

from rest_framework.routers import SimpleRouter


# настройка роутов для модели Ad
from ads.views import AdViewSet

ads_router = SimpleRouter()

# в роуте мы регистрируем ViewSet, который импортирован из приложения Djoser
ads_router.register("ads", AdViewSet, basename="ads")


urlpatterns = [
    path("", include(ads_router.urls)),
]

