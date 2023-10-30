from rest_framework import serializers
from .models import Student
class Student_Serielizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

    # def create(self, validated_data):
    #     return Student.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name=validated_data.get('name',instance.name)
    #     instance.roll_number=validated_data.get('roll_number',instance.roll_number)
    #     instance.department=validated_data.get('department',instance.department)
