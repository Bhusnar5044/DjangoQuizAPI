from django.urls import path
from . import views
# from django.conf.urls import handler404, handler500

urlpatterns = [
    path('quiz/', views.postQuiz, name='postquiz'),
    path('quiz/:<int:quiz_id>/', views.getQuiz, name='getquiz'),
    path('questions/:<int:question_id>/', views.getQuestions, name='getquestions'),
    path('questions/', views.postQuestions, name='postquestions'),
]

# handler404 = views.error_404
# handler500 = views.error_500
