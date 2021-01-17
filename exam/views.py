from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
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
from rest_framework import status



class TaskView(ListModelMixin,
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
            instance.score += 10
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
            instance.score += 10
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




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def reciver(request):

    if request.method == 'GET':
        try:
            user = request.GET["user"]
            student = Student.objects.get(key=user)
            if not student.level_4:
                student.level_4 = True
                student.score += 20
                student.save(update_fields=["level_4", "score"])
                
        except:
            content = {'error_message': 'даний ключ для запиту або запитуємий користувач не існує'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return Response({'score': student.score,'next_hint': student.hint_4_level, 'special_data': student.special_data})

    elif request.method == 'POST':
        print(request.data)
        try:
            user = request.data["user"]
            student = Student.objects.get(key=user)
            if not student.level_5:
                student.level_5 = True
                student.score += 20
                student.save(update_fields=["level_5", "score"])
            student.special_data = request.data["special_data"]
            student.save(update_fields=["special_data"])

        except:
            content = {'error_message': 'даний ключ для запиту або запитуємий користувач не існує'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
                
        return Response({'score': student.score,'next_hint': student.hint_5_level, 'special_data': student.special_data})


    elif request.method == "DELETE":
        try:
            user = request.data["user"]
            student = Student.objects.get(key=user)
            if not student.level_6:
                student.level_6 = True
                student.score += 30
                student.save(update_fields=["level_6", "score"])
            student.special_data = ""
            student.save(update_fields=["special_data"])

        except:
            content = {'error_message': 'даний ключ для запиту або запитуємий користувач не існує'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        return Response({'score': student.score,'next_hint': student.hint_6_level, 'special_data': student.special_data})



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def test(request):
    if request.method == 'GET':
        return Response({"method": "GET"})

    if request.method == 'POST':
        return Response({"method": "POST"})

    if request.method == 'PUT':
        return Response({"method": "PUT"})
    
    if request.method == 'DELETE':
        return Response({"method": "DELETE"})
        
