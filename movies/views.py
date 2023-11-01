from django.shortcuts import render, redirect
from django.db.models import Q

from . models import Movie


def index(request):
    movie = Movie.objects.all()
    context = {
        'movie':movie,
        'user':request.user,
    }
    return render(request, 'index.html',context)

def ticket_rate(request):
    return render(request, 'ticket-rate.html')


def contact_us(request):
    return render(request, 'contact_us.html')

def about_us(request):
    return render(request, 'about-us.html')


def purchase_ticket(request, movie_id):
    user = request.user
    moive = Movie.objects.get(id=movie_id)
    print(moive.name)
    if user.is_authenticated:
        return redirect('contact_us') 
    
def search(request):
    moive = None
    keyword = None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            moive = Movie.objects.filter(Q(name__icontains=keyword) | Q(description__icontains=keyword))
            print(moive)
        else:
            pass
    context = {
        'moive':moive,
    }
    return redirect('index')