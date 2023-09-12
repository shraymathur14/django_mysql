from rest_framework import serializers
from .models import Department,Employee

class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields="__all__"

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"