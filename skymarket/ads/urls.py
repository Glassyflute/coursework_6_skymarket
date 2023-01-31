from django.urls import include, path

from rest_framework.routers import SimpleRouter

from ads.models import Ad
from ads.views import CommentViewSet, AdDetailView, AdListView, AdCreateView, AdUpdateView, AdDeleteView, AdImageView, \
    AdMyView

# TODO настройка роутов для модели
# from ads.views import AdViewSet

# ads_router = SimpleRouter()
# ads_router.register("ads", AdViewSet, basename="ads")
#
comments_router = SimpleRouter()
comments_router.register("comments", CommentViewSet, basename="comments")


urlpatterns = [
    path("", AdListView.as_view()),
    path("<int:pk>/", AdDetailView.as_view()),
    path("me/", AdMyView.as_view()),

    path("create/", AdCreateView.as_view()),
    path("<int:pk>/update/", AdUpdateView.as_view()),
    path("<int:pk>/upload_image/", AdImageView.as_view()),
    path("<int:pk>/delete/", AdDeleteView.as_view()),

    # path("<int:pk>/", include(comments_router.urls)),
]

urlpatterns += [path("<int:ad_pk>/", include(comments_router.urls))]
# urlpatterns += [path(
#     "<int:ad_pk>/comments/my_list/", CommentViewSet.as_view({"get": "list"})
# )]

# ad = AdDetailView.get_object(request)
# urlpatterns += [path(f"ads/{ad.pk}/", include(comments_router.urls))]

# from django.urls import include, path
#
# from rest_framework.routers import SimpleRouter
#
#
# # настройка роутов для модели Ad
# from ads.views import AdViewSet
#
# ads_router = SimpleRouter()
#
#
# ads_router.register("ads", AdViewSet, basename="ads")
#
#
# urlpatterns = [
#     path("", include(ads_router.urls)),
# ]




