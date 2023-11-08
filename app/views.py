from django.shortcuts import render
from django.http import HttpResponse

def mno(request):
    return HttpResponse('<h1><marquee>hi hello namaste</marquee></h1>')
