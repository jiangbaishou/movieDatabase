from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import MatchAll, MoviePeople, MovieCompany, MovieDetail

# Create your views here.
def index(request):
	movieList = MatchAll.objects.filter(movieid__lte = 5)
	return render(request, 'movies/list.html', {'movie_list': movieList})


#movie_detail
def movie_detail(request, movieId):
	"""
	Given a movieId, return movie detail data in json format, if not exists, return None.
	"""
	try:
		movieDetail = MovieDetail.objects.get(pk = int(movieId))
		movieDetail = serializers.serialize('json', [movieDetail])
	except ObjectDoesNotExist:
		movieDetail = None
	return HttpResponse(movieDetail, content_type = 'application/json')
#end of movie_detail


#movie_people
def movie_people(request, movieId):
	"""
	Given a movieId, return movie people data in json format, if not exists, return None.
	"""
	try:
		moviePeople = MoviePeople.objects.filter(movieid = int(movieId))
		moviePeople = serializers.serialize('json', moviePeople)
	except Exception as e:
		print(e)
		moviePeople = None
	return HttpResponse(moviePeople, content_type = 'application/json')
#end of movie_people


#movie_company
def movie_company(request, movieId):
	"""
	Given a movieId, return movie company data in json format, if not exists, return None.
	"""
	try:
		movieCompany = MovieCompany.objects.filter(movieid = int(movieId))
		movieCompany = serializers.serialize('json', movieCompany)
	except Exception as e:
		print(e)
		movieCompany = None
	return HttpResponse(movieCompany, content_type = 'application/json')
#end of movie company
		
