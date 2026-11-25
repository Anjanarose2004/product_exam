from rest_framework import serializers
from productapp.models import ProductDb
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductDb
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['username','email','password'] 

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data) 
        return user          