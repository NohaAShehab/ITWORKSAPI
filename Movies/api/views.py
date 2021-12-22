from django.http import HttpResponse
from Movies.models import Movie, WatchList
from Movies.api.serializer import MovieSerializer, WatchListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics



# equested as api

###
# @api_view()
# def movie_list(request):
#     movies = Movie.objects.all()
#     movies_serailizer = MovieSerializer(movies, many=True)
#     return Response(movies_serailizer.data)

# GET, POST
@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == 'POST':
        serial_movie = MovieSerializer(data=request.data)
        if serial_movie.is_valid():
            serial_movie.save()
            print("test")
            return Response(serial_movie.data)

    movies = Movie.objects.all()
    movies_serailizer = MovieSerializer(movies, many=True)
    return Response(movies_serailizer.data)


### update, delete, view
@api_view(["GET", "PUT", "DELETE"])
def single_movie(request, id):
    movie = Movie.objects.get(pk=id)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    if request.method == 'PUT':
        movie_ser = MovieSerializer(movie, data=request.data)
        if movie_ser.is_valid():
            movie_ser.save()
            return Response(movie_ser.data)

    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
# class MovieListAPIVIEW(APIView):
#     def get(self, request, format=None):
#         movies = Movie.objects.all()
#         movies_serailizer = MovieSerializer(movies, many=True)
#         return Response(movies_serailizer.data)
#
#     def post(self, request):
#         serial_movie = MovieSerializer(data=request.data)
#         if serial_movie.is_valid():
#             serial_movie.save()
#             print("test")
#             return Response(serial_movie.data)


class MovieListAPIVIEW(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIVIEW(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    lookup_url_kwarg = 'id'
    queryset = Movie.objects.all()


class WatchListAPIVIEW(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

class WatchListDetailAPIVIEW(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WatchListSerializer
    lookup_url_kwarg = 'id'
    queryset = WatchList.objects.all()
# class MovieDetailAPIVIEW(APIView):
#
#     def get(self, request, id):
#         movie = Movie.objects.get(pk=id)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         movie = Movie.objects.get(pk=id)
#         movie_ser = MovieSerializer(movie, data=request.data)
#         if movie_ser.is_valid():
#             movie_ser.save()
#             return Response(movie_ser.data)
#
#     def delete(self, request, id):
#         movie = Movie.objects.get(pk=id)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)






