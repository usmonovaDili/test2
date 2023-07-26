from django.shortcuts import render
from django.http import HttpResponse

def info(request):
    return HttpResponse('hello django')



def poll(request):
    return  HttpResponse('hello python')
