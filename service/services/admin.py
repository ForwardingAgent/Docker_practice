from django.contrib import admin

from services.models import Service
from services.models import Plan
from services.models import Subscription

# 3 видео 20:00 создаем admin.site.register(...) чтобы можно было из админки создавать модели Клиента и тд
admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(Subscription)
