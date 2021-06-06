from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required, login_required

from ..forms import questionForm
from ..models import Quiz, Question


@login_required
@permission_required('is_superuser')
def admin_questions_view(request,pk):
    quiz = Quiz.objects.get(id = pk)
    all_questions = Question.objects.filter(quiz_name__id = pk)
    context = {'all_questions' : all_questions , 'quiz' : quiz }
    return render(request,"questions/adminquestions.html", context)

@login_required
@permission_required('is_superuser')
def create_question(request, pk):
    quiz = Quiz.objects.get(id = pk)
    if request.method == "POST":
        form = questionForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.quiz_name = quiz
            temp.save()
            return redirect('createquestion',quiz.id)
    form = questionForm()
    context = {'form': form ,'quiz': quiz, "val":"Create"}
    return render(request,"questions/createquestion.html", context) 

@login_required
@permission_required('is_superuser')
def update_question(request, pk):
    question = Question.objects.get(id = pk)
    form = questionForm(instance= question)
    if request.method == "POST":
        form = questionForm(request.POST, instance= question)
        if form.is_valid():
            form.save()
            return redirect("adminquestions",question.quiz_name.id)
    context = {'form': form,'quiz': question.quiz_name, "val": "Change"}
    return render(request,"questions/createquestion.html", context) 

@login_required
@permission_required('is_superuser')
def delete_question(request, pk):
    question = Question.objects.get(id = pk)
    question.delete()
    return redirect("adminquestions",question.quiz_name.id)