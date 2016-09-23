from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import MatchAll

# Create your views here.
def index(request):
	movieList = MatchAll.objects.filter(movieid__lte = 5)
	return render(request, 'movies/list.html', {'movie_list': movieList})

