from django.shortcuts import render, HttpResponse
from password.models import Data


# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        data = Data(name=name, password=password)
        data.save()
    return render(request, 'index.html')

