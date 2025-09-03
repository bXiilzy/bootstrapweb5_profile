from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def for_view(request):
    context = {}
    context['message'] = "การวนซ้ำใน_Django"
    
    if request.method == 'POST' and request.POST.get('count') != '':
        number = int(request.POST.get('count'))
        context['count'] = list(range(1,number +1))
    else:
        context['count'] = list(range(1, 2))
   
    return render(request, 'for.html',context)

def table_view(request):
    context = {}
    context['message'] = "ตารางสูตรคูณ"
    
    if request.method == 'POST' and request.POST.get('number') != '':
        number = int(request.POST.get('number'))
        context['number'] = number
        context['table'] = [(i, number * i) for i in range(1, 13)]
    else:
        context['table'] = []
        context['number'] = None
        
    return render(request, 'table.html', context)

def students_view(request):
    from .models import Students
    context = {}
    context['title'] = "รายชื่อนักเรียน"
    
    strdents = Students.objects.all()
    context['students'] = strdents
    return render(request, 'students.html', context)


def subjects(request):
    from .models import Subjects
    context = {}
    context['title'] = "รายวิชา"
    subjects_list = Subjects.objects.all()
    context['subjects'] = subjects_list
    return render(request, 'subjects.html', context)

