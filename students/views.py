from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    context={
        "title":"Clarusway",
        "desc":"This is a description",
        "number":"1111",
        
    }
    
    return render(request,"students/home.html",context)
