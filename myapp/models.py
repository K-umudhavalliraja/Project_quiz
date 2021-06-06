from django.db import models

# Create your models here.


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
        
class Question(models.Model):
    
    ANS_CHOICES = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D')
    )

    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=100, verbose_name= "question")
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length = 1 ,choices=ANS_CHOICES)

    def __str__(self):
        return self.question_title

