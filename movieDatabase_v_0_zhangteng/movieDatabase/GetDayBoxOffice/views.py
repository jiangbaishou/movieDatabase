from django.shortcuts import render
from django.http import HttpResponse
from .movie_data_query_date import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getDayBoxoffice(request,dateStr):
	return HttpResponse(data_if_effective(dateStr))
