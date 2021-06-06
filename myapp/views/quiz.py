from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required, login_required

from ..forms import quizForm 
from ..models import Quiz

@login_required
@permission_required('is_superuser')
def admin_quiz_view(request):
    all_quiz = Quiz.objects.order_by('id')
    if request.method == "POST":
        form = quizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminquiz')
    form = quizForm()
    context = {"all_quiz" : all_quiz, "form":form }
    return render(request,"quiz/adminquiz.html",context)

@login_required
@permission_required('is_superuser')
def update_quiz(request,pk):
    all_quiz = Quiz.objects.order_by('id')
    quiz = Quiz.objects.get(id=pk)
    form = quizForm(instance = quiz)
    if request.method == "POST":
        form = quizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect("adminquiz")
    context = {"all_quiz" : all_quiz, "form":form , "update": "update"}
    return render(request,"quiz/adminquiz.html",context)

@login_required
@permission_required('is_superuser')
def delete_quiz(request,pk):
    quiz = Quiz.objects.get(id=pk)
    quiz.delete()
    return redirect('adminquiz')

def logoutview(request):
    logout(request)
    return redirect('home')