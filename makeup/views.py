from django.shortcuts import render

def index(request):
    return render(request, 'makeup/index.html')

# Create your views here.
