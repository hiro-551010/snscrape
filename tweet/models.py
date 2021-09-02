from django.db import models

class PersonModel(models.Model):
    username = models.CharField("ユーザーID", max_length=20)
    
    class Meta:
        db_table = "PersonModel"


class KeywordModel(models.Model):
    keyword = models.CharField("キーワード", max_length=30)
    since = models.CharField("いつから", max_length=10)
    until = models.CharField("いつまで", max_length=10)

    class Meta:
        db_table = "KeywordModel"
