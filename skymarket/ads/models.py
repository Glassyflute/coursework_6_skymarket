from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True, blank=True)
    author = models.ForeignKey("users.User", related_name="ads", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ad/images/', null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]
    # *Все записи при выдаче должны быть отсортированы по дате создания
    # (чем новее, тем выше).*

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=1000)
    author = models.ForeignKey("users.User", related_name="comments", on_delete=models.CASCADE, null=True)
    ad = models.ForeignKey(Ad, related_name="ads", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]

    def __str__(self):
        return self.text

