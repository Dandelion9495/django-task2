from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Books
from .serializers import *

@api_view(['GET'])
def get_books(request):
    queryset = Books.objects.all()
    serializer = BooksSerializer(queryset, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def create_books(request):
    # print('=============')
    # print(request)
    # print(request.data)
    # print('=============')
    serializer = BooksSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)



@api_view(['GET'])
def get_books_by_id(request, pk):
    try:
        cat = Books.objects.get(id=pk)
        serializer = BooksSerializer(cat)
        return Response(serializer.data, status=200)
    except Books.DoesNotExist:
        return Response('Not Found')


@api_view(['PUT'])
def update_books(request, pk):
    try:
        cat = Books.objects.get(id=pk)
        serializer = BooksSerializer(instance=cat, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    except Books.DoesNotExist:
        return Response('Not Found')


@api_view(['DELETE'])
def delete_books(request, pk):
    try:

        cat = Books.objects.get(id=pk)
        cat.delete()
        return Response('Successfully deleted', status=200)
    except Books.DoesNotExist:
        return Response('Not Found')