from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'password', 'email', 'image', 'role']


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'password', 'email', 'image', 'role']


# class UserRegistrationSerializer(BaseUserRegistrationSerializer):
# 	    class Meta:
# 	        model = User
# 	        fields = ['first_name', 'last_name', 'phone',
# 	                  'password', 'email', 'image']
#
# class CurrentUserSerializer(serializers.ModelSerializer):
# 	    class Meta:
# 	        model = User
# 	        fields = ['first_name', 'last_name', 'phone', 'image']