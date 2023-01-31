from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import Ad, Comment
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
    # permission_classes = [IsAuthenticated]


class AdMyView(ListAPIView):
    """
    Список всех объявлений по пользователю, который залогинен с токеном.
    """

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author_id=self.request.user.pk)


class AdListView(ListAPIView):
    """
    Список всех объявлений
    """
    serializer_class = AdSerializer
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
    serializer_class = AdDetailSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        author_pk = self.request.user.pk
        serializer.save(author_id=author_pk)




class AdUpdateView(UpdateAPIView):
    """
    Обновление данных по объявлению
    """
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    # permission_classes = [IsAuthenticated, IsAdAuthorOrStaff]

    # def perform_update(self, serializer):
    #     curr_user_pk = self.request.user.pk
    #
    #     ad_pk = self.kwargs.get("ad_pk")
    #     if ad_pk in
    #
    #
    #     ad = Ad.objects.filter(pk=ad_pk)
    #
    #     if curr_user_pk == ad.author.pk:
    #         serializer.save()



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
    # permission_classes = [IsAuthenticated, IsAdAuthorOrStaff]


class CommentViewSet(viewsets.ModelViewSet):
    """
    Класс с комментариями к объявлению с использованием Router и сериализатора
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # список комментариев или конкретный коммент-й по выбранному объявлению
    def get_queryset(self):
        ad_pk = self.kwargs.get("ad_pk")
        return Comment.objects.filter(ad_id=ad_pk)

    def perform_create(self, serializer):
        ad_pk = self.kwargs.get("ad_pk")
        author_pk = self.request.user.pk
        serializer.save(author_id=author_pk, ad_id=ad_pk)


    # все комментарии пользователя, который под токеном, по разным объявлениям
    # @action(detail=False)
    # def my_list(self, request, *args, **kwargs):
    #     self.queryset = Comment.objects.filter(author_id=request.user.pk)
    #     return super().list(self, request, *args, **kwargs)

