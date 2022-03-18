from django.shortcuts import render

# Create your views here.


def volah_home(request):
    return render(request, 'volah/volah_home.html')
