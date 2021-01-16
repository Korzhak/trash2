from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.decorators import api_view
from .models import Student, Task
from .serializer import (
    Student1LevelSerializer,
    Student2LevelSerializer,
    Student3LevelSerializer,
    Student4LevelSerializer,
    Student5LevelSerializer,
    TaskSerializer
)
from rest_framework.decorators import api_view
from rest_framework.response import Response


class TaskView(RetrieveModelMixin,
               GenericViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class Student1LevelView(RetrieveModelMixin,
                        GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = Student1LevelSerializer

    def retrieve(self, request, *args, **kwargs):
        super(Student1LevelView, self).retrieve(request, *args, **kwargs)
        instance = self.get_object()

        if not instance.level_1:
            instance.level_1 = True
            instance.score += 10
            instance.save(update_fields=["level_1", "score"])

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class Student2LevelView(RetrieveModelMixin,
                        GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = Student2LevelSerializer

    def retrieve(self, request, *args, **kwargs):
        super(Student2LevelView, self).retrieve(request, *args, **kwargs)
        instance = self.get_object()

        if not instance.level_2:
            instance.level_2 = True
            instance.score += 20
            instance.save(update_fields=["level_2", "score"])

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class Student3LevelView(RetrieveModelMixin,
                        GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = Student3LevelSerializer

    def retrieve(self, request, *args, **kwargs):
        super(Student3LevelView, self).retrieve(request, *args, **kwargs)
        instance = self.get_object()

        if not instance.level_3:
            instance.level_3 = True
            instance.score += 30
            instance.save(update_fields=["level_3", "score"])

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class Student4LevelView(RetrieveModelMixin,
                        GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = Student4LevelSerializer

    def retrieve(self, request, *args, **kwargs):
        super(Student4LevelView, self).retrieve(request, *args, **kwargs)
        instance = self.get_object()

        if not instance.level_4:
            instance.level_4 = True
            instance.score += 40
            instance.save(update_fields=["level_4", "score"])

        serializer = self.get_serializer(instance)
        return Response(serializer.data)




@api_view(['GET', 'POST'])
def reciver(request):

    if request.method == 'GET':
        return Response({'something': 'my custom JSON'})

    elif request.method == 'POST':
        print(request.data)
        return Response({'something': 'my custom JSON'})


