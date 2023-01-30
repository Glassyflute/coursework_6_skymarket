from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView

from users.models import User


@method_decorator(csrf_exempt, name="dispatch")
class UserImageView(UpdateView):
    """
    Добавление/обновление картинки в профиле пользователя
    """
    model = User
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES.get("image")
        self.object.save()

        return JsonResponse({
                    "id": self.object.pk,
                    "email": self.object.email,
                    "image": self.object.image.url if self.object.image else None
                })

