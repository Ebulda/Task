from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer



@api_view(['GET', 'POST'])
def task_view(request):
    if request.method == 'GET':
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail_api_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    else:
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

