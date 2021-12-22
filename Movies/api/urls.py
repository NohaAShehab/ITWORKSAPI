
from django.urls import path
from  Movies.api.views import movie_list, single_movie,\
    MovieListAPIVIEW,MovieDetailAPIVIEW, WatchListAPIVIEW, WatchListDetailAPIVIEW

urlpatterns=[
    # path("list",movie_list,name="movielist"),
    path("list", MovieListAPIVIEW.as_view(),name="movielist"),
    # path("list/<int:id>", single_movie, name="singlemovie"),
    path("list/<int:id>", MovieDetailAPIVIEW.as_view(), name="singlemovie"),
    path("watchlist", WatchListAPIVIEW.as_view(), name="watchlist"),
    path("watchlist/<int:id>", WatchListDetailAPIVIEW.as_view(), name="singlewatchlist"),

]

