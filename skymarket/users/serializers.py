from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'password', 'email', 'image', 'role']


class CurrentUserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, user):
        return str(user.image)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'phone', 'image']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'phone', 'image']
