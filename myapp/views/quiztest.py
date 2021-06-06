from django.shortcuts import render

from ..models import Quiz, Question
from datetime import datetime


def home(request):
    quizzes = Quiz.objects.all()
    return render(request,"index.html",{"quizzes":quizzes})


def get_timeTaken(startTime,endTime):
    start = datetime.fromisoformat(startTime)
    end = datetime.fromtimestamp(endTime)
    timeTaken = end - start 
    temp = str(timeTaken).rsplit('.',1)
    return temp[0]


def get_result(mark, totalmark):
        result = round(mark/totalmark * 100)
        if result >= 50 : return "Pass" 
        return "Fail" 


def quiz_test_view(request,pk):
    quiz = Quiz.objects.get(id = pk)
    if request.method == "POST":
        tempavailableQ = request.POST.get('availableQ')
        availableQ = [int(i) for i in (tempavailableQ.lstrip('[').rstrip(']').split(', '))]
        availableQ.remove(int(request.POST.get('currentQ')))
        qNo = int(request.POST.get('qNo')) + 1
        mark = request.POST.get('mark')
        startTime = request.POST.get('startTime')
        if not availableQ:
            endTime = float(request.POST.get("endTime"))
            timeTaken = get_timeTaken(startTime, endTime)
            total_mark = quiz.question_set.all().count()
            result = get_result(int(mark) , total_mark)
            context = {"timeTaken": timeTaken ,"totalmark": total_mark, "mark": mark, "result" :result}
            return render(request,"quiz/quizresults.html",context)
    else:    
        questions = quiz.question_set.all()
        availableQ = []
        mark = 0
        qNo = 1
        startTime = str(datetime.now())
        for Q in questions:
            availableQ.append(Q.id)
    lastQ = False
    if availableQ :
        question = Question.objects.get(id= availableQ[0])
        if len(availableQ) == 1:
            lastQ = True
    else:
        question = None
    context = {"question" :question, "qNo": qNo, "availableQ" : availableQ , "mark" : mark , "startTime" : startTime, "lastQ" : lastQ }
    return render(request, "questions/testquestions.html",context)