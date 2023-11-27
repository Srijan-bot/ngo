from django.shortcuts import render,redirect
from .models import Service,Faq

# Create your views here.
def index(request):
    servs = Service.objects.all()
    faq = Faq.objects.all()
    return render(request,'index.html', {'servs': servs,'faq':faq})
def contri(request):
    return render(request,'contri.html')
def about(request):
    return render(request,'about.html')
