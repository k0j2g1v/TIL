from django.shortcuts import render, redirect
from .models import Movie, Comment
# Create your views here.
def index(request):
    movies = Movie.objects.all()[::-1]
    context = {'movies': movies}
    return render(request,'movies/index.html',context)
   
# 사용자로 부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
  if request.method == 'POST':  
    title = request.POST.get('title')
    title_en = request.POST.get('title_en')
    audience = request.POST.get('audience')
    open_date = request.POST.get('open_date')
    genre = request.POST.get('genre')
    watch_grade = request.POST.get('watch_grade')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre,
    watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    movie.save()
    return redirect(f'/movies/{movie.pk}')
  else:
    # 사용자에게 게시글 작성 폼을 보여줌
    return render(request,'movies/create.html')
# 게시글 상세정보를 가져오는 함수
def detail(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {'movie': movie}
    return render(request, 'movies/detail.html',context)

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('/movies/')

# # 사용자한테 게시글 수정 폼을 전달
# def edit(request, movie_pk):
#     movie = Movie.objects.get(pk=movie_pk)
#     context={'movie': movie}
#     return render(request,'Movies/edit.html',context)

# 수정 내용 전달받아서 DB에 저장(반영)
def update(request, movie_pk):
  movie=Movie.objects.get(pk=movie_pk)
  if request.method == 'POST':
    movie.title=request.POST.get('title')
    movie.title_en=request.POST.get('title_en')
    movie.audience=request.POST.get('audience')
    movie.open_date=request.POST.get('open_date')
    movie.genre=request.POST.get('genre')
    movie.watch_grade=request.POST.get('watch_grade')
    movie.score=request.POST.get('score')
    movie.poster_url=request.POST.get('poster_url')
    movie.description=request.POST.get('description')
    movie.save()
    #return render(request,'articles/index.html')
    return redirect(f'/movies/{movie.pk}')
  else:    
    context={'movie': movie}
    return render(request,'Movies/edit.html',context)

def comment_create(request,  movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  if request.method == 'POST':
    content = request.POST.get('content')
    comment = Comment(movie=movie,content=content)
    comment.save()
    return redirect('movies:detail', movie_pk)
  else:
    return redirect('movies:detail', movie_pk)

# 댓글 삭제 뷰 함수
def comment_delete(request, movie_pk, comment_pk):
  # article = Article.objects.get(pk=article_pk)
  # comment = Comment.objects.get(pk=comment_pk)
  if request.method == 'POST':
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', movie_pk)
  else:  
    return redirect('articles:detail', movie_pk)
  


  