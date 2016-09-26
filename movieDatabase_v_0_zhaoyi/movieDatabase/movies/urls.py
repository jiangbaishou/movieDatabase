from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.index, name = 'index'),
				#movie detail
				url(r'^movie_detail/(?P<movieId>[0-9]+)/$', views.movie_detail, name = 'movie_detail'),
				#movie people
				url(r'^movie_people/(?P<movieId>[0-9]+)/$', views.movie_people, name = 'movie_people'),
				#movie company
				url(r'^movie_company/(?P<movieId>[0-9]+)/$', views.movie_company, name = 'movie_company')]

