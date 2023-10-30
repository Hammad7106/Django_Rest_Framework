from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serielizers import Student_Serielizer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.
#I have created API Views by using DRF
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def api(request,pk=None):
    if request.method=="GET":
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serielizer=Student_Serielizer(stu)
            return Response(serielizer.data)

        stu=Student.objects.all()
        serielizer=Student_Serielizer(stu,many=True)
        return Response(serielizer.data)

    if request.method=="POST":
        serielizer=Student_Serielizer(data=request.data)
        if serielizer.is_valid():
            serielizer.save()
            return Response({'msg':'Data Created'})

        return Response(serielizer.errors)

    if request.method=="PUT":
        id=pk
        stu=Student.objects.get(pk=id)
        serielizer=Student_Serielizer(stu,data=request.data)
        if serielizer.is_valid():
            serielizer.save()
            return Response({'msg':'Data Updated'})

        return Response(serielizer.errors)

    if request.method=="PATCH":
        id=pk
        stu=Student.objects.get(pk=id)
        serielizer=Student_Serielizer(stu,data=request.data,partial=True)
        if serielizer.is_valid():
            serielizer.save()
            return Response({'msg':'PATCH Data Updated'})

        return Response(serielizer.errors)

    if request.method=="DELETE":
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

















def student_list(request):
    get_data=Student.objects.all()
    serielized_data=Student_Serielizer(get_data,many=True)
    return JsonResponse(serielized_data.data,safe=False)





# @csrf_exempt  # Use this decorator for simplicity in this example; consider a more secure approach in production.
# def student_api(request):
#     if request.method == "GET":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id = python_data.get('id', None)  # Retrieve 'id' from query parameters
#
#         if id is not None:
#             try:
#                 stu = Student.objects.get(id=id)
#                 serializer = Student_Serielizer(stu)
#                 return JsonResponse(serializer.data)
#             except Student.DoesNotExist:
#                 return JsonResponse({'error': 'Student not found'}, status=404)
#         students = Student.objects.all()
#         serializer = Student_Serielizer(students, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     if request.method=="POST":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         serielizer=Student_Serielizer(data=python_data)
#
#         if serielizer.is_valid():
#             serielizer.save()
#             res={'msg':'Data Created'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,'application/json')
#
#         json_data=JSONRenderer().render(serielizer.errors)
#         return HttpResponse(json_data,'application/json')
#
#     if request.method=="PUT":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id')
#         stu=Student.objects.get(id=id)
#         serielizer=Student_Serielizer(stu,data=python_data)
#
#         if serielizer.is_valid():
#             serielizer.save()
#             res={'msg':'Data Updated'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#
#         json_data=JSONRenderer().render(serielizer.errors)
#         return HttpResponse(json_data,content_type='application/json')
#
#     if request.method=="DELETE":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         res={'msg':'Data Deleted Successfully'}
#         json_data=JSONRenderer().render(res)
#         return HttpResponse(json_data,content_type='application/json')





