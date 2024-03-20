from rest_framework import serializers
from.models import Employee,LeaveManagement,Profile


class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class Leaveserializer (serializers.ModelSerializer):
    class Meta:
        model=LeaveManagement
        fields='__all__'

class Profileserializer (serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=["empid","empname","DOJ","email","designation","avl_leaves"]