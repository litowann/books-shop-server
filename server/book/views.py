from django.shortcuts import render
from .models import Book
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BookSerializer


class BookView(APIView):
    def get(self, request):
        output = [{
            "name": output.name,
            "pages": output.pages,
            "author": output.author,
            "year": output.year
        } for output in Book.objects.all()]

        return Response(output)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data)