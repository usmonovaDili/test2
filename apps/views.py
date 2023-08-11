from datetime import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from .models import TODO
from .serializers import TODOSerializers
from rest_framework.views import APIView


# Create your views here.


class AllTodosView(APIView):
    def get(self, request, *args, **kwargs):
        todos = TODO.objects.all()
        serializers = TODOSerializers(todos, many=True)
        return Response(serializers.data)


class AllToDoViews(APIView):
    def get(self, request):
        todo = TODO.objects.all()
        serializers = TODOSerializers(todo, many=True)
        return Response(serializers.data)


class CreateToDoViews(APIView):
    def get_all(self, request):
        serializer = TODOSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class UpdateToDoViews(APIView):
    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TODOSerializers(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class DeleteTodoViews(APIView):
    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ToDoQueryViews(APIView):
    def get(self, request):
        status = request.query_params.get('status', True)
        day = request.query_params.get('day', None)
        data = datetime.strptime(day, '%y-%m-%d').date()
        todo = TODO.objects.filter(create_at=data, status=status)
        serializer = TODOSerializers(todo, many=True)
        return Response(serializer.data)
