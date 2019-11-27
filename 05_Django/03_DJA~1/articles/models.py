from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    # 원래대로라면 새로운 필드를 추가하고 나면 makemigrations 할때, 어떤값을 넣을건지
    # Django가 물어본다. 기본적으로 blank=False이기 때문이다
    # blank=True -> '빈문자열'이 들어가도 된다.
    image = ProcessedImageField(
      processors=[Thumbnail(200,300)],  # 처리할 작업
      format='JPEG',                 # 이미지 포멧
      options={'quality':90},        # 각종 추가 옵션
      upload_to='articles/images',   # 저장 위치
      # 실제 경로 -> MEDIA_ROOT/articles/images
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 표시 형식 수정
    def __str__(self):
        return f'[{self.pk}] {self.title}' 
    
class Comment(models.Model):
  # related_name : 부모 테이블에서 역으로 참조할 때 기본적으로 모델이름_set 형식으로 불러온다.
  # related_name 이라는 값을 설정해서 _set 명령어를 임의로 변경할 수 있다.
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  content = models.CharField(max_length=250)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # Model Level 에서 Metadata 설정
  class Meta:
    ordering = ['-pk',]

  def __str__(self):
    return self.content