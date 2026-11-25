from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from productapp import serializers
from productapp.models import ProductDb
from rest_framework import authentication,permissions
from rest_framework.permissions import IsAuthenticated
from productapp.serializers import ProductSerializer,UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
# Create your views here.
class SignupView(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            user=serializer_instance.save()
            token,created=Token.objects.get_or_create(user=user)
            return Response({
                "message":"created",
                "token":token.key
            })
        return Response({"message":"error"},status=400)

class ProductListCreateView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]


    def get(self,request):
        product=ProductDb.objects.all()
        serializer_instance=ProductSerializer(product,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=ProductSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message":"product create"},status=201)
        return Response({"message":"invalid"},status=400)

class ProductDetailDeleteView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        product=get_object_or_404(ProductDb,pk=pk)
        serializer_instance=ProductSerializer(product)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):
        product=get_object_or_404(ProductDb,pk=pk)
        serializer_instance=ProductSerializer(product,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message":"product updated"})
        return Response({"message":"error"})
    def delete(self,request,pk):
        product=get_object_or_404(ProductDb,pk=pk)
        product.delete()
        return Response({"message":"deleted"})
