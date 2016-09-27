from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import MatchAll, MoviePeople, MovieCompany, MovieDetail, MovieDaily
import json

# Create your views here.
#index page
def index(request):
	movieList = MatchAll.objects.filter(movieid__lte = 5)
	return render(request, 'movies/list.html', {'movie_list': movieList})
#end of index


#movie_detail
def movie_detail(request, movieId):
	"""
	#Given a movieId, return movie detail data in json format, if not exists, return None.
	This is the page for movie detail, utilizing detail.html.
	"""
	try:
		#.values() method make the result a dictionary object
		movieDetail = MovieDetail.objects.values().get(pk = int(movieId))
		#movieDetail = serializers.serialize('json', [movieDetail])
	except ObjectDoesNotExist:
		movieDetail = None
	#return HttpResponse(movieDetail, content_type = 'application/json')
	return render(request, 'movies/detail.html', {'movieDetail': movieDetail})
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


#movie_daily
def movie_daily(request, movieId):
	"""
	Given a movieId, return movie daily data in json format, if not exists, return None.
	"""
	try:
		movieDaily = MovieDaily.objects.filter(movieid = int(movieId))
		#we want to merge with MovieDetail in order to get a movie's gross
		try:
			movieDetail = MovieDetail.objects.get(pk = int(movieId))
			movieGross = movieDetail.gross
		except ObjectDoesNotExist:
			movieGross = None
		#print(movieGross)
		#add gross into movieDaily
		movieDaily = json.dumps({'data': serializers.serialize('json', movieDaily), 'movieGross': movieGross})
	except Exception as e:
		print(e)
		movieDaily = None
	return HttpResponse(movieDaily, content_type = 'application/json')
#end of movie_daily


#movie_search
def movie_search(request):
	"""
	Given a movie name, we search it in MovieDetail. If exists, we return the similar movie list.
	"""
	search_text = request.GET.get('q') #in django, we don't have request.args.get as in Flask
	try:
		similarMovies = MovieDetail.objects.filter(moviename__icontains = str(search_text)) | MovieDetail.objects.filter(alias__icontains = str(search_text))
		similarMovies = similarMovies.values_list('movieid', 'moviename')
		search_results = []
		for obj in similarMovies:
			search_results.append({'moviename': obj[1], 'movieid': obj[0]})
		#similarMovies = [obj.movieid, obj.moviename for obj in similarMovies]
		#similarMovies = serializers.serialize('json', similarMovies)
		#print(similarMovies)
	except Exception as e:
		print(e)
		similarMovies = None
	return HttpResponse(json.dumps({"results": search_results}), content_type = 'application/json')
	#return JsonResponse(json.dumps(similarMovies), safe = True)
#end of movie_search

