from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse

# Create your views here.
def inserttopic(request):
    tm=TopicModelForm()
    d={'tm':tm}
    if request.method=='POST':
        tmfod=TopicModelForm(request.POST)
        if tmfod.is_valid():
            tmfod.save()
            return HttpResponse('data inserted')
    return render(request,'inserttopic.html',d)
        
     


def insertwebpage(request):
    wo=WebpageModelForm()
    d={'wo':wo}
    if request.method=='POST':
        tmfod=WebpageModelForm(request.POST)
        if tmfod.is_valid():
            tmfod.save()
            return HttpResponse('data inserted')
    return render(request,'insertwebpage.html',d)