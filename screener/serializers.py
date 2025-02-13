from rest_framework import serializers
from .models import Cv 


class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cv
        fields = '__all__'
