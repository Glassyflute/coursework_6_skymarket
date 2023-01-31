from rest_framework import serializers
from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SerializerMethodField()

    def get_author_first_name(self, comment):
        return comment.author.first_name

    author_last_name = serializers.SerializerMethodField()

    def get_author_last_name(self, comment):
        return comment.author.last_name

    author_image = serializers.SerializerMethodField()

    def get_author_image(self, comment):
        return str(comment.author.image)

    class Meta:
        model = Comment
        fields = ["pk", "text", "author_id", "ad_id", "created_at",
                  "author_first_name", "author_last_name", "author_image"]


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description", "author_id"]


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SerializerMethodField()

    def get_author_first_name(self, ad):
        return ad.author.first_name

    author_last_name = serializers.SerializerMethodField()

    def get_author_last_name(self, ad):
        return ad.author.last_name

    phone = serializers.SerializerMethodField()

    def get_phone(self, ad):
        return str(ad.author.phone)

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description",
                  "author_first_name", "author_last_name", "author_id"]


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

