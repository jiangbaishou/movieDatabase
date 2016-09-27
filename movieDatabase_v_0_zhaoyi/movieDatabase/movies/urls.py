from django.conf.urls import url
from . import views

app_name = 'movies'
urlpatterns = [url(r'^$', views.index, name = 'index'),
				#movie detail
				url(r'^movie_detail/(?P<movieId>[0-9]+)/$', views.movie_detail, name = 'movie_detail'),
				#movie people
				url(r'^movie_people/(?P<movieId>[0-9]+)/$', views.movie_people, name = 'movie_people'),
				#movie company
				url(r'^movie_company/(?P<movieId>[0-9]+)/$', views.movie_company, name = 'movie_company'),
				#movie daily
				url(r'^movie_daily/(?P<movieId>[0-9]+)/$', views.movie_daily, name = 'movie_daily'),
				#movie search
				url(r'^movie_search/$', views.movie_search, name = 'movie_search')]

