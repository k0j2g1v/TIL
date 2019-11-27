from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    image = models.ImageField(blank=True)
    # image = ProcessedImageField(
    #     processors=[Thumbnail(200, 300)],   # 처리할 작업
    #     format='JPEG',                  # 이미지 포맷
    #     options={'quality': 90},        # 각종 추가 옵션
    #     upload_to='articles/images',    # 저장 위치
    #     # 실제 경로 -> MEDIA_ROOT/articles/images
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk',]

    def __str__(self):
        return self.content