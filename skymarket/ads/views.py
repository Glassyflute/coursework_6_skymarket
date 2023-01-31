from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Ad, Comment
from ads.permissions import IsObjectAuthorOrStaff
from ads.serializers import AdSerializer, CommentSerializer, AdDetailSerializer, AdListSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


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
    permission_classes = [IsAuthenticated]


class AdMyView(ListAPIView):
    """
    Список всех объявлений по пользователю, который залогинен с токеном.
    """

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author_id=self.request.user.pk)


class AdListView(ListAPIView):
    """
    Список всех объявлений
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        title = self.request.GET.get("title")
        if title:
            self.queryset = self.queryset.filter(title__icontains=title)
        return self.queryset


class AdCreateView(CreateAPIView):
    """
    Создание нового объявления
    """
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        author_pk = self.request.user.pk
        serializer.save(author_id=author_pk)


class AdUpdateView(UpdateAPIView):
    """
    Обновление данных по объявлению
    """
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated, IsObjectAuthorOrStaff]


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
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated, IsObjectAuthorOrStaff]


class CommentViewSet(viewsets.ModelViewSet):
    """
    Класс с комментариями к объявлению
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # список комментариев или конкретный коммент-й по выбранному объявлению (ad_pk)
    def get_queryset(self):
        ad_pk = self.kwargs.get("ad_pk")
        return Comment.objects.filter(ad_id=ad_pk)

    # получаем автоматом данные по pk для пользователя и объявления при создании коммента
    def perform_create(self, serializer):
        ad_pk = self.kwargs.get("ad_pk")
        author_pk = self.request.user.pk
        serializer.save(author_id=author_pk, ad_id=ad_pk)

    default_permissions = [AllowAny()]
    permissions = {
        "retrieve": [IsAuthenticated()],
        "update": [IsAuthenticated(), IsObjectAuthorOrStaff()],
        "partial_update": [IsAuthenticated(), IsObjectAuthorOrStaff()],
        "destroy": [IsAuthenticated(), IsObjectAuthorOrStaff()]
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permissions)


