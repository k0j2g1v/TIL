from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def index(request):
    students = Student.objects.all()[::-1]
    context = {'students': students}
    return render(request,'students/index.html',context)
# 사용자에게 게시글 작성 폼을 보여주는 함수
def new(request):
    return render(request,'students/new.html')
# 사용자로 부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
    name = request.POST.get('name')
    birth =request.POST.get('birth')

    student = Student(name=name, birth=birth)
    student.save()
    return redirect(f'/students/{student.pk}')

# 게시글 상세정보를 가져오는 함수
def detail(request,student_pk):
    student = Student.objects.get(pk=student_pk)
    context = {'student': student}
    return render(request, 'students/detail.html',context)

def delete(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    student.delete()
    return redirect('/students/')

# 사용자한테 게시글 수정 폼을 전달
def edit(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    context={'student': student}
    return render(request,'students/edit.html',context)

# 수정 내용 전달받아서 DB에 저장(반영)
def update(request, student_pk):
    student=Student.objects.get(pk=student_pk)
    student.name=request.POST.get('name')
    student.birth=request.POST.get('birth')
    student.save()
    

    #return render(request,'articles/index.html')
    return redirect(f'/students/{student.pk}')