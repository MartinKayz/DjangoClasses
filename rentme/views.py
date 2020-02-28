from django.shortcuts import render
from django.template import loader
from rentme.myform import myform
from django import forms

# Create your views here.
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET"])
def index(request):
    # template = loader.get_template('index.html')
    # name = {
    #     'student':'Kubona'
    # }
    # return HttpResponse(template.render())
    # return render(request,'index.html')
    stu =myform()
    return render(request,"index.html",{'form':stu})


def hello(request):
    return HttpResponse('<h1>This is Http GET request.</h1>')
    