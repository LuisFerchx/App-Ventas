from django.shortcuts import render

from django.views import generic

# Create your views here.
#las clases empiezan con mayuscula la primera letra
#la herencia va entre parentesis
class Home(generic.TemplateView):
    template_name = 'bases/home.html'
