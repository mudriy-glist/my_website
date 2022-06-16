import re
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "backend/index.html")

def playground(request):
    return render(request, "backend/playground.html")