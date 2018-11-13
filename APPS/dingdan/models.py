import random
import time

from django.contrib.auth.models import User
from django.db import models

from APPS.account.models import Book


class DingDan(models.Model):
    dd_id = models.AutoField(primary_key=True, auto_created=True)
    dingdan_number = models.CharField(max_length=255)
    user_id = models.ForeignKey("auth.User", models.DO_NOTHING, db_column='user_id')
    book_id = models.ForeignKey("account.Book", models.DO_NOTHING, db_column='book_id')
    is_pay = models.IntegerField(default=0)

    class Meta:
        db_table = "dingdan"
