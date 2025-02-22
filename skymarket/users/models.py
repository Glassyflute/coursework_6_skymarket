from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager, UserRoles
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone = PhoneNumberField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(max_length=15, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to='profile/images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    # константа USERNAME_FIELD определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # константа REQUIRED_FIELDS содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # переопределяем менеджер объектов
    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]

    def __str__(self):
        return self.email
