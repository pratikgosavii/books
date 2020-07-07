from django.shortcuts import render
from cart.models import cart

# Create your views here.






def index(request):



    dests = cart.objects.filter( owner = request.user)

    context= {

        'dests' : dests
        
    }

    return render(request, 'index.html', context)
