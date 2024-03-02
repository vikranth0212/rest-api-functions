from rest_framework import serializers
from app.models import *
class SchoolModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields='__all__'
        #fields=['Scname']

#this file we are created manually, serailizers is used to convert ORM code to Json format.        