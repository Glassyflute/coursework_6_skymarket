from django.urls import include, path

from rest_framework.routers import SimpleRouter
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


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api-auth/', include('rest_framework.urls')),
#     path('', views.root),
#     path('ad/', include('ads.urls.ad')),
#     path('cat/', include('ads.urls.cat')),
#     path('user/', include('ads.urls.user')),
#     path('selection/', include('ads.urls.selection')),
# ]

# urlpatterns = [
#     path('', views.AdListView.as_view()),
#     path('<int:pk>/', views.AdDetailView.as_view()),
#     path('create/', views.AdCreateView.as_view()),
#     path('<int:pk>/update/', views.AdUpdateView.as_view()),
#     path('<int:pk>/upload_image/', views.AdImageView.as_view()),
#     path('<int:pk>/delete/', views.AdDeleteView.as_view()),
# ]

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

# from django.urls import include, path
#
# from rest_framework.routers import SimpleRouter
#
#
# # настройка роутов для модели Comment
# from ads.views import CommentViewSet
#
# comments_router = SimpleRouter()
#
#
# comments_router.register("comments", CommentViewSet, basename="comments")
#
#
# urlpatterns = [
#     path("", include(comments_router.urls)),
# ]


