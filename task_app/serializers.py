from rest_framework import serializers
from .models import Task
from rest_framework.exceptions import ValidationError


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    completed = serializers.BooleanField()
    created = serializers.IntegerField()

    class Meta:
        model = Task
        fields = 'title description completed created'.split()