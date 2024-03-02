from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view,permission_classes

#in rest_framework package there is a modules
# decorators from that we imported api_view,permission_classes,
#permissions from that we imported IsAuthenticated
#isauthenticated allows normal and adminuser(superuser)

from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def schoolJsonData(request):

    #it will get all the school table objects
    SOD=School.objects.all()

    #it will convert orm object to json objects 
    JOD=SchoolModelSerializer(SOD,many=True)

    #object means it will give address but data means it will give like string

    #here we are converting objects into data
    jsondata=JOD.data

    return Response(jsondata)