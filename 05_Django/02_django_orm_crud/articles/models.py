from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체를 표시하는 형식 커스터마이징
    def __str__(self):
        return f'[{self.pk}번글]: {self.title}|{self.content}'