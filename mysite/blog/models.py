# Create your models here.
from django.db import models
from django.utils import timezone
from django.db import models

# Create your models here.
#필드 개수가 다르다.

class Post(models.Model):
    #이 Post의 저자이다라는 의미, CASCADE : 종속이라는 의미
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #블로그 기사의 제목
    text = models.TextField()  # 글자수에 제한 없는 텍스트
    #생성자를 만들때마다, 반드시 필수 파라미터가 존재해야한다.
    created_date = models.DateTimeField(
        default=timezone.now)  # 날짜와 시간
    #Null Field를 허용
    published_date = models.DateTimeField(
        blank=True, null=True) #  필드가 폼에서 빈 채로 저장되는 것을 허용, null은 DB 관점

    def publish(self):
        #published_data를 지금날짜로 바꾸고 save
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title