from django.shortcuts import render
from.models import Employee,LeaveManagement,Profile
from.serializer import Employeeserializer,Leaveserializer,Profileserializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST','GET','PUT','DELETE'])
def Employee_data(request):
    if request.method=='POST':
        serializer=Employeeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    #return Response(status=status.HTTP_201_CREATED)

    elif request.method=='GET':
        employee_details=Employee.objects.all()
        serializer =Employeeserializer(employee_details,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='PUT':
        employee_details =Employee.objects.get(empid=request.data['empid'])
        serializer=Employeeserializer(employee_details,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method=='DELETE':
        employee_details =Employee.objects.get(empid=request.data['empid'])
        employee_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def Leave_data(request):
    if request.method == 'POST':
        serializer =Leaveserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST','GET'])
def Profile_data(request):
    if request.method=='POST':
        serializer=Profileserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    #return Response(status=status.HTTP_201_CREATED)

    elif request.method=='GET':
        profile_details=Profile.objects.all()
        serializer=Profileserializer(profile_details,many=True)
        return Response(serializer.data)




