from django.db import models
from django.core.validators import MaxValueValidator
from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    # PositiveIntegerField - число, скидка по подписке  
    full_price = models.PositiveIntegerField()


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    # PositiveIntegerField - число, скидка по подписке 
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[
                                                       MaxValueValidator(100)
                                                   ])


class Subscription(models.Model):  # 3 видео 13:10
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT) 
    # related_name - то имя с которым наша модел (класс Subscription) будет доступна внутри модели (Client) с которой мы тут образуем связь
    # т.е. чтобы посмотреть все подписки клиента надо написать Client.subscriptions.all это при related_name
    # второй способ посмотреть все подписки клиента: subscription.filter(client=client.id).all
    service = models.ForeignKey(Service, related_name='subscription', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscription', on_delete=models.PROTECT)
