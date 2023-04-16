from django.shortcuts import render, HttpResponse
from .models import CreditUnion
# Create your views here.
def hello(request):
    creditunions=CreditUnion.objects.all()
    context = {
        'creditunions':creditunions,
    }
    return render(request,'index.html',context)
