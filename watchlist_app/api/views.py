from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


# Class based API view


class MovieListAV(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializers = MovieSerializer(movies, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailAV(APIView):

    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                {
                    'error': "Movie Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                {
                    'error': "Movie Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = MovieSerializer(data=request.data, instance=movie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                {
                    'error': "Movie Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#  function based api view

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializers = MovieSerializer(movies, many=True)
#         return Response(serializers.data)
#
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 {
#                     'error': "Movie Not Found"
#                 },
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 {
#                     'error': "Movie Not Found"
#                 },
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = MovieSerializer(data=request.data, instance=movie)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 {
#                     'error': "Movie Not Found"
#                 },
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
