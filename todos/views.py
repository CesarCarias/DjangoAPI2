from django.shortcuts import render
from todos.serializers import TaskSerializer
from rest_framework import generics
from todos.models import Task
# Create your views here.
class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer