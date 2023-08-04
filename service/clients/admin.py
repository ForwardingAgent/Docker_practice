from django.contrib import admin

# 3 видео 20:00 создаем admin.site.register(...) чтобы можно было из админки создавать модели Клиента и тд
from clients.models import Client

admin.site.register(Client)
