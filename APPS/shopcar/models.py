import random

from django.db import models
from django.contrib.auth.models import User

from APPS.account.models import Book

rand = random.randint(50, 150)


class Shopcar(models.Model):
    car_id = models.AutoField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey("auth.User", models.DO_NOTHING, db_column='user_id')
    book_id = models.ForeignKey('account.Book', models.DO_NOTHING, db_column='book_id')
    count = models.IntegerField()
    price = models.IntegerField(default=rand)
    is_delete = models.IntegerField(default=0)

    class Meta:
        db_table = "shop_car"
