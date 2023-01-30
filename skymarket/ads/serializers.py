from rest_framework import serializers
from ads.models import Comment, Ad


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):

    # author = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field="username"
    # )
    # category = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field="name"
    # )
    #
    # location_names = serializers.SerializerMethodField()
    #
    # def get_location_names(self, ad):
    #     return [location_elem.name for location_elem in ad.author.location_names.all()]

    class Meta:
        model = Ad
        fields = '__all__'



class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

    # author = serializers.SlugRelatedField(
    #     slug_field="username",
    #     queryset=AdUser.objects.all()
    # )
    # category = serializers.SlugRelatedField(
    #     slug_field="name",
    #     queryset=Category.objects.all()
    # )
    #
    # location_names = serializers.CharField()
    #
    # class Meta:
    #     model = Ad
    #     fields = ["id", "name", "price", "description", "image", "is_published", "author", "category", "location_names"]


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]