from rest_framework import pagination, viewsets

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    """
    Класс с объявлениями с использованием Router и сериализатора
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    Класс с комментариями к объявлениям с использованием Router и сериализатора
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

