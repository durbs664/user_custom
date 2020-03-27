from django.shortcuts import render
from day1.models import Question
# Create your views here.

def ghar_bahira(request):
    context = {}
    # # print(request.headers)
    # #      'some_string' : "This is passed in the view"
    # #  }
    # list_values = ['manip' , 'ram', 'shyam']
    # # list_values.append("manip")
    # # list_values.append("ram")
    # # list_values.append("shyam")
    # context['list_values'] = list_values
    questions = Question.objects.all()
    context['questions'] = questions
    return render(request,"day1/home.html",context)
