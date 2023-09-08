from rest_framework import serializers
from .models import Dataphone

class DataphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dataphone
        fields="__all__"