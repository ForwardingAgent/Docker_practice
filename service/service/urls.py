"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from services.views import SubscriptionView

urlpatterns = [
    path('admin/', admin.site.urls),
]

# 3 видео 34;00 routers - 
router = routers.DefaultRouter()
router.register(r'api/subscription', SubscriptionView)
# 3 видео 35:00 передаем SubscriptionView (наследованое от ReadOnlyModelViewSet в services.views.py) в router т.е. в DefaultRouter(), и он будет сам генерировать url

urlpatterns += router.urls
# добавляются url от роутера 