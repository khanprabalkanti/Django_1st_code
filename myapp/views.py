from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def register(request):
    return render(request, 'register.html')
def register(request):
    return render(request, 'new/new.html')

