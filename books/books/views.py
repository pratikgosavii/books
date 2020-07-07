from django.shortcuts import render
from home.models import books
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.





def contacts(request):

    return render(request, 'index.html')