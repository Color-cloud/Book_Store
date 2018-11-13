from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


class Classify(models.Model):
    classify_id = models.IntegerField(primary_key=True)
    classify_name = models.CharField("小说分类", max_length=64, )

    class Meta:
        db_table = "classify"


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    img_url = models.CharField("图片网址", max_length=200)
    book_name = models.CharField("书名", max_length=200)
    writer = models.CharField("作者", max_length=64)
    miaoshu = UEditorField(verbose_name="书籍简介", width=1000, height=600,
                           imagePath="media/arts_ups/ueditor/",
                           filePath="media/arts_ups/ueditor/",
                           blank=True, toolbars="full", default='')
    classify_id = models.ForeignKey("Classify", models.DO_NOTHING, db_column="classify_id")

    class Meta:
        db_table = "Book"


class BookDetail(models.Model):
    zhangjie = models.CharField("章节目录", max_length=64)
    text = UEditorField(verbose_name="小说正文", width=1000, height=600,
                        imagePath="media/arts_ups/ueditor/",
                        filePath="media/arts_ups/ueditor/",
                        blank=True, toolbars="full", default='')
    book_id = models.ForeignKey("Book", models.DO_NOTHING, db_column="book_id")

    class Meta:
        db_table = "BookDetail"
