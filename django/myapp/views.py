from django.shortcuts import render
from myapp.models import office

# Create your views here.

def uhome(request):
    var=office.objects.all()
    return render(request,'home.html',{'var':var})