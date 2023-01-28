from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этого рекомендуется использовать SimpleRouter


users_router = SimpleRouter()

# в роуте мы регистрируем ViewSet, который импортирован из приложения Djoser
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]

# в итоге мы получаем необходимые urls:
# GET "users/" — список профилей пользователей
# POST "users/" — регистрация пользователя
# GET, PATCH, DELETE "users/{id}" — в соотвествии с REST и необходимыми permissions (для администратора)
# GET PATCH "users/me" — получение и изменение своего профиля
# POST "users/set_password" — ручка для изменения пароля

# POST "users/reset_password" — ручка для направления ссылки сброса пароля на email*
# POST "users/reset_password_confirm" — ручка для сброса своего пароля*

# Помимо пользователя, осталось подключить авторизацию по токену.
# /jwt/create/ (JSON Web Token Authentication) -- из документации
# /jwt/refresh/ (JSON Web Token Authentication

# Это также можно сделать с помощью Djoser, однако оставим это для самостоятельного изучения и выберем
# простой вариант — использование библиотеки `djangorestframework-simplejwt`.


