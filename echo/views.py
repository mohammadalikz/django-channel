from django.shortcuts import render
def index(request):
    return render(request , 'echo/index.html')
# Create your views here.
