# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Quiz, Questions
from .serializers import QuizSerializer, QuestionsSerializer
# from django.core.exceptions import ObjectDoesNotExist 
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json, requests, jsonpath


def getQuiz(request,quiz_id):
    try:
        data={}
        quiz=Quiz.objects.get(id=quiz_id)
        if quiz:
            ser=QuizSerializer(quiz)
            data=ser.data
            return JsonResponse(data, safe=False)
    except Exception:
        return JsonResponse(data, safe=False)

def postQuiz(request):
    url = "http://localhost:8080/"
    file=open('E:\\djangoProjects\\test-113-q-9d6542f202e64713a85e8b8ee9666c98--django-2.1-p-3.6-in-docker\\restapi\\json\\quizPost.json','r')
    json_input=file.read()
    request_json=json.loads(json_input)
    r=requests.post(url, json=request_json)

    json_response = json.loads(r.request.body)
    
    # data=r.request.body
    name=json_response['name']
    descr=json_response['description']
    q=Quiz()
    q.name=name
    q.description=descr
    q.save()

    try:
        data={}
        quiz=Quiz.objects.all()
        if quiz:
            ser=QuizSerializer(quiz, many=True)
            data=ser.data
            return JsonResponse(data, safe=False)
    except Exception:
        data['status']='failure'
        data['reason']='bad request'
        return JsonResponse(data, safe=False)
    # return HttpResponse(json_response)

def getQuestions(request,question_id):
    try:
        data={}
        question=Questions.objects.get(pk=question_id)
        if question:
            ser=QuizSerializer(question)
            data=ser.data
            return JsonResponse(data, safe=False)
    except Exception:
        return JsonResponse(data, safe=False)

def postQuestions(request):
    url = "http://localhost:8080/"
    file=open('E:\\djangoProjects\\test-113-q-9d6542f202e64713a85e8b8ee9666c98--django-2.1-p-3.6-in-docker\\restapi\\json\\questions.json','r')
    json_input=file.read()
    request_json=json.loads(json_input)
    r=requests.post(url, json=request_json)

    json_response = json.loads(r.request.body)
    
    # data=r.request.body
    name=json_response['name']
    options=json_response['options']
    correct_option=json_response['correct_option']
    quiz=json_response['quiz']
    points=json_response['points']
    q=Questions()
    q.name=name
    q.options=options
    q.correct_option=correct_option
    q.quiz=quiz
    q.points=points
    q.save()

    try:
        data={}
        quiz=Questions.objects.all()
        if quiz:
            ser=QuestionsSerializer(quiz, many=True)
            data=ser.data
            return JsonResponse(data, safe=False)
    except Exception:
        data['status']='failure'
        data['reason']='bad request'
        return JsonResponse(data, safe=False)
    # return HttpResponse(json_response)



# # def error_404(request):
# #         data = {}
# #         # return render(request,'myapp/error_404.html', data)
# #         return JsonResponse(data, safe=False)

# # def error_500(request):
# #         data = {}
# #         # return render(request,'myapp/error_404.html', data)
# #         return JsonResponse(data, safe=False)