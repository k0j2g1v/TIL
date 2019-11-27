from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=40)
    title_en = models.CharField(max_length=40)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=40)
    watch_grade = models.CharField(max_length=40)
    score = models.FloatField()
    poster_url = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    
class Comment(models.Model):
  # related_name : 부모 테이블에서 역으로 참조할 때 기본적으로 모델이름_set 형식으로 불러온다.
  # related_name 이라는 값을 설정해서 _set 명령어를 임의로 변경할 수 있다.
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  content = models.CharField(max_length=250)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # Model Level 에서 Metadata 설정
  class Meta:
    ordering = ['-pk',]

  def __str__(self):
    return self.content
  