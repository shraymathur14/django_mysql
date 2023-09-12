from django.shortcuts import render
from .models import Department, Employee
from .serializers import DeptSerializer, EmpSerializer

# used to access our api by others
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

@csrf_exempt
# Create your views here.
def deptapi(request,id=0):
    if request.method=='GET':
        departments = Department.objects.all()
        departments_serializer=DeptSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DeptSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Department.objects.get(D_ID=department_data['D_ID'])
        departments_serializer=DeptSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        department=Department.objects.get(D_ID=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    

@csrf_exempt
def empapi(request,id=0):
    if request.method=="GET":
        emp=Employee.objects.all()
        emp_ser=EmpSerializer(emp,many=True)
        return JsonResponse(emp_ser.data,safe=False)
    
    elif request.method=="POST":
        my_data=JSONParser().parse(request)
        emp_ser=EmpSerializer(data=my_data)
        if emp_ser.is_valid():
            emp_ser.save()
            return JsonResponse("ADDED Successfully",safe=False)
        else:
            return JsonResponse("Failed to add",safe=False)
    
    elif request.method=="PUT":
        my_data=JSONParser().parse(request)
        emp_data=Employee.objects.get(E_ID=my_data["E_Id"])
        emp_ser=EmpSerializer(my_data,data=emp_data)
        if emp_ser.is_valid():
            emp_ser.save()
            return JsonResponse("Updated Successfully",safe=False)
        else:
            return JsonResponse("Failed to add",safe=False)
    
    elif request.method=="DELETE":
        obj=Employee.objects.get(E_ID=id)
        obj.delete()
        return JsonResponse("Deleted",safe=False)

    