from django.http import JsonResponse
from django.urls import resolve
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework import pagination, viewsets
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer, AdDetailSerializer, AdListSerializer, AdDestroySerializer


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
# class AdViewSet(viewsets.ModelViewSet):
#     """
#     Класс с объявлениями с использованием Router и сериализатора
#     """
#     queryset = Ad.objects.all()
#     serializer_class = AdSerializer


class AdDetailView(RetrieveAPIView):
    """
    Детальная информация по выбранному объявлению, доступна при аутентификации пользователя по токену.
    """
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    # permission_classes = [IsAuthenticated]


class AdMyView(ListAPIView):
    """
    Список всех объявлений по пользователю, который залогинен с токеном.
    """

    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author_id=self.request.user.pk)


class AdListView(ListAPIView):
    """
    Список всех объявлений
    """
    serializer_class = AdListSerializer
    queryset = Ad.objects.all()

    def get_queryset(self, *args, **kwargs):
        title = self.request.GET.get("title")
        if title:
            self.queryset = self.queryset.filter(title__icontains=title)
        return self.queryset

    # queryset = Ad.objects.annotate(
    #     location_names=F('author__location_names__name')
    # ).order_by("-price")

    # permission_classes = [AllowAny]


class AdCreateView(CreateAPIView):
    """
    Создание нового объявления
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    # permission_classes = [IsAuthenticated]


class AdUpdateView(UpdateAPIView):
    """
    Обновление данных по объявлению
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    # permission_classes = [IsAuthenticated, IsAdAuthorOrStaff]


@method_decorator(csrf_exempt, name="dispatch")
class AdImageView(UpdateView):
    """
    Добавление/обновление картинки в объявлении
    """
    model = Ad
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get("image")
        self.object.save()

        return JsonResponse({
                    "id": self.object.pk,
                    "title": self.object.title,
                    "image": self.object.image.url if self.object.image else None
                })


class AdDeleteView(DestroyAPIView):
    """
    Удаление объявления
    """
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
    # permission_classes = [IsAuthenticated, IsAdAuthorOrStaff]









class CommentViewSet(viewsets.ModelViewSet):
    """
    Класс с комментариями к объявлению с использованием Router и сериализатора
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(ad_id=self.request.user.pk)

    def list(self, request, *args, **kwargs):
        ad_pk = self.request.GET.get('ad_pk', None)
        self.queryset = Comment.objects.filter(ad_id=ad_pk)
        return super().list(request, *args, **kwargs)


    # def get_queryset(self):
    #
    #     ad_pk = self.request.resolver_match.kwargs.get("comment.ad.pk")
    #     self.queryset = Comment.objects.filter(ad_id=ad_pk)
    #     return self.queryset


    # def get_queryset(self):
    #     ad_pk = self.request.GET.get('ad_pk', None)
    #     self.queryset = Comment.objects.filter(ad_id=ad_pk)
    #     return self.queryset



#
# def ad_pk_obtain(self, request):
#     ad_pk = request.resolver_match.kwargs.get("ad_id")
#     return ad_pk

