from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    # 3 видео, к каждому юзеру в системе будет соответствовать модель (класс) Client
    # on_delete - при удалении юзера проверит если связаные с ним модели Client и если есть то не даст удалить эту модель юзера
    company_name = models.CharField(max_length=100)
    full_address = models.CharField(max_length=100)
