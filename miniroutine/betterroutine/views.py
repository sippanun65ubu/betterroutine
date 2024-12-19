from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def habitlist(request):
    return render(request, 'habitlist.html')