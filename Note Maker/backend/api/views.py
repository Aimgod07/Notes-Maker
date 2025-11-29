from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NotesSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Notes

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



class NotesListCreateView(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]
     
    
    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)  
    def perform_create(self, serializer):
        if serializer.is_valid():
         serializer.save(author=self.request.user)
        else:
           print("Serializer is not valid")
    
class NotesDeleteView(generics.DestroyAPIView):
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

    

