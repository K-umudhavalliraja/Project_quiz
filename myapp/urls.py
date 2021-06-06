from django.urls import path
from django.contrib.auth import views
from .views import questions, quiz, quiztest


urlpatterns = [
    
    path("",quiztest.home, name = "home"),
    path("quiz/test/<int:pk>/", quiztest.quiz_test_view, name = "quiztest" ),

    path("quiz/", quiz.admin_quiz_view , name = "adminquiz"),
    path("quiz/update/<int:pk>/", quiz.update_quiz, name = "updatequiz" ),
    path("quiz/delete/<int:pk>/", quiz.delete_quiz, name = "deletequiz" ),

    path("quiz/questions/<int:pk>/", questions.admin_questions_view, name = "adminquestions" ),
    path("question/create/<int:pk>/", questions.create_question, name = "createquestion" ),
    path("question/update/<int:pk>/", questions.update_question, name = "updatequestion" ),
    path("question/delete/<int:pk>/", questions.delete_question, name = "deletequestion" ),

    path("login/",views.LoginView.as_view(), name='login'),
    path("logout/",quiz.logoutview , name = "logout"),

    ]
