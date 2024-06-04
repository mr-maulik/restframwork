from django.shortcuts import render
from .models import studinfo 
from .serializer import studserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        stdata=studinfo.objects.all()
        serial=studserializer(stdata,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serial=studserializer(stid)
    return Response(serial.data,status=status.HTTP_200_OK)

@api_view(['DELETE','GET'])
def deleteid(request, id):
    try:
        stid = studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=studserializer(stid)
        return Response(serial.data,status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        stid.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def savedata(request):
    if request.method == 'POST':
        serial=studserializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

