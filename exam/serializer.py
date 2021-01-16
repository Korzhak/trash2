from rest_framework import serializers
from .models import Student, Group, Specialization, Flow, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("description",)


class FlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flow
        fields = ("name",)


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ("name",)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)


class StudentSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    flow = FlowSerializer(read_only=True,)
    specialization = SpecializationSerializer(read_only=True,)

    class Meta:
        model = Student
        fields = (
            "full_name", "group", "flow", "specialization",
            "attendance", "academic_performance",
            "date_of_birth", "photo"
        )


class Student1LevelSerializer(StudentSerializer):
    class Meta:
        model = Student
        fields = (
            "full_name", "hint_1_level", "score"
        )


class Student2LevelSerializer(StudentSerializer):
    class Meta:
        model = Student
        fields = (
            "full_name", "group", "flow", "specialization",
            "date_of_birth", "photo", "hint_2_level", "score"
        )


class Student3LevelSerializer(StudentSerializer):
    class Meta:
        model = Student
        fields = (
            "attendance", "academic_performance",
            "crystals", "coins", "score", "hint_3_level"
        )


class Student4LevelSerializer(StudentSerializer):
    class Meta:
        model = Student
        fields = (
            "joke", "score", "hint_4_level"
        )


class Student5LevelSerializer(StudentSerializer):
    class Meta:
        model = Student
        fields = (
            "joke", 
        )