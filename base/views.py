from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

#function based view
# def home(request):
#     return render(request,'base/index.html',)

#class based view
class Home(TemplateView):
    template_name = 'base/index.html'

class About(TemplateView):
    template_name = 'base/about.html'