from django.shortcuts import render
from django.http import HttpResponse
from PageApp.forms import *
from PageApp.models import *

# Create your views here.


def HomeView(request):

    return render(request, "home.html")



def SongsView(request):

    if request.method == "POST":

        form = SongsForm(request.POST)

        if form.is_valid():

            info_dict = form.cleaned_data

            newSong = Songs(
                name = info_dict["name"],
                artist = info_dict["artist"],
                year = info_dict["year"]
            )

            newSong.save()

            return render(request, "home.html")
    else:
        
        form = SongsForm()

    return render(request, "songs.html", {"formulario":form})



def PlayersView(request):

    if request.method == "POST":

        form = PlayersForm(request.POST)

        if form.is_valid():

            info_dict = form.cleaned_data

            newPlayer = Players(
                name = info_dict["name"],
                age = info_dict["age"],
                sport = info_dict["sport"],
                country = info_dict["country"],
                team= info_dict["team"]

            )

            newPlayer.save()

            return render(request, "home.html")
    else:
        
        form = PlayersForm()

    return render(request, "players.html", {"formulario":form})



def MoviesView(request):

    if request.method == "POST":

        form = MoviesForm(request.POST)

        if form.is_valid():

            info_dict = form.cleaned_data

            newMovie = Movies(
                name = info_dict["name"],
                protagonist = info_dict["protagonist"],
                year = info_dict["year"],
                streaming = info_dict["streaming"]
            )

            newMovie.save()

            return render(request, "home.html")
    else:
        
        form = MoviesForm()

    return render(request, "movies.html", {"formulario":form})


def SearchPlayers(request):

    if request.GET:

        name = request.GET["name"]
        players = Players.objects.filter(name__icontains=name)

        message = f"We are looking for the player {name}"

        return render(request, "home.html", {"players":players})
    
    else:
        
        message = f"You didn't send data"

        return HttpResponse(message)




