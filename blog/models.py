from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    # 다른 모델에 대한 링크를 의미
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 글자 수가 제한된 텍스트를 정의
    title = models.CharField(max_length=200)
    # 글자 수가 제한이 없는 텍스트
    text = models.TextField()
    # 날짜와 시간
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    # 메서드
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title