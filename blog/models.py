from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author: 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    # 목록에서 각각의 페이지로 들어가는 링크 자동 생성
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'