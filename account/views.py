from django.shortcuts import render
from rest_framework import serializers
from .models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response

# Create your views here.
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
    def create(self, data):
        newuser = User.objects.create_user(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            password = data['password'],
            image = data['image']
        )
        
        return newuser

        
        

class signupView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    
class UserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    permission_classes = [IsAuthenticated]
    

class fetchUser(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = userSerializer
    
    def get(self, request):
        print(request.user.id)
        
        user = User.objects.get(id = request.user.id)
        serializers = self.serializer_class(user)
        
        return Response(data = serializers.data, status=200)
    


