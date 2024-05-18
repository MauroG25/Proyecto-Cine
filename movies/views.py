from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import timedelta
from django.core import serializers

from .models import User, Movie,CinemaHall,Ticket

def index(request):
    return render(request, "movies/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "movies/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "movies/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "movies/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "movies/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "movies/register.html")
    
def bestongoingindex(request):
    bestongoing_movies = Movie.objects.filter(
        release_date__lte=timezone.now(), 
        end_date__gte=timezone.now()
    ).order_by('-rating')[:5]
    data = json.loads(serializers.serialize('json', bestongoing_movies))
    return JsonResponse(data, safe=False)

def ongoingindex(request):
    ongoing_movies = Movie.objects.filter(
        release_date__lte=timezone.now(), 
        end_date__gte=timezone.now()
    ).order_by('-release_date')[:7]
    data = json.loads(serializers.serialize('json', ongoing_movies))
    return JsonResponse(data, safe=False)

def upcomingindex(request):
    upcoming_movies = Movie.objects.filter(
       release_date__gte=timezone.now(), 
       release_date__lte=timezone.now() + timedelta(days=30)
    ).order_by('release_date')[:7]
    data = json.loads(serializers.serialize('json', upcoming_movies))
    return JsonResponse(data, safe=False)

def ongoing(request):
    ongoing_movies = Movie.objects.filter(
        release_date__lte=timezone.now(), 
        end_date__gte=timezone.now()
        
        
    ).order_by('-release_date')


    
    paginator = Paginator(ongoing_movies, 14)

    
    page_number = request.GET.get('page', 1)

    
    page = paginator.get_page(page_number)
    ongoing_movies = page.object_list

    data = json.loads(serializers.serialize('json', ongoing_movies))
    return JsonResponse(data, safe=False)

def ongoingrender(request):
    return render(request, "movies/cartelera.html")

def upcoming(request):
    upcoming_movies = Movie.objects.filter(
       release_date__gte=timezone.now(), 
       release_date__lte=timezone.now() + timedelta(days=30)
       #show only 5
    ).order_by('release_date')
    

    paginator = Paginator(upcoming_movies, 14)

    
    page_number = request.GET.get('page', 1)

    
    page = paginator.get_page(page_number)
    upcoming_movies = page.object_list

    data = json.loads(serializers.serialize('json', upcoming_movies))
    return JsonResponse(data, safe=False)

@login_required
def upcomingrender(request):
    
    return render(request, "movies/proximo.html", {
    }) 

@login_required #to buy a ticket
def movieview(request, movie_id):
    user = request.user
    try: 
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return render(request, "movies/404.html")
    if request.method == "POST":
        if request.POST.get("seats") is not None:
            seats = int(request.POST.get("seats"))
            if movie.cinemahall.available_seats >= seats:
                # Create a new ticket
                Ticket.objects.create(user=user, movie=movie, seats=seats)

                # Decrease the number of available seats
                movie.cinemahall.available_seats -= seats
                movie.cinemahall.save()

                message = f"You bought {seats} ticket(s) for {movie.title}!"
            else:
                message = "There are not enough available seats."

    return render(request, "movies/movie.html", {
        "movie": movie,
        "message": message if 'message' in locals() else ""
    })
