from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import SimpleRouter
from djoser.views import UserViewSet

# TODO здесь необходимо подключит нужные нам urls к проекту

# router = routers.SimpleRouter()
# router.register('location', LocationViewSet)


# users_router = SimpleRouter()
# # в роуте мы регистрируем ViewSet, который импортирован из приложения Djoser
# users_router.register("users", UserViewSet, basename="users")

# ads_router = SimpleRouter()
# ads_router.register("ads", AdViewSet, basename="ads")


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema")),

    # path("ad/", include("ads.urls.ad")),
    path("api/ads/", include("ads.urls")),
    # path("", include(ads_router.urls)),

    # path("comment/", include("ads.urls.comment")),

    path("api/", include("users.urls")),
    # path("api/userr/", include(users_router.urls)),

    path("api/token/", TokenObtainPairView.as_view()),
    path("api/refresh/", TokenRefreshView.as_view()),
]

# urlpatterns += users_router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
