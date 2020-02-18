from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    userid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    hobby = models.CharField(max_length=20)

#user id와 슬래시, 유저 이름을 추가할 예정
    def __str__(self):
        #return self.userid + "/" + self.age
        return f"{self.userid}/{self.name}/{self.age}"
