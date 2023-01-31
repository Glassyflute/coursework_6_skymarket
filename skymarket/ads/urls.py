from django.urls import include, path

from rest_framework.routers import SimpleRouter

from ads.views import CommentViewSet, AdDetailView, AdListView, AdCreateView, AdUpdateView, AdDeleteView, AdImageView, \
    AdMyView


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
]

urlpatterns += [path("<int:ad_pk>/", include(comments_router.urls))]





