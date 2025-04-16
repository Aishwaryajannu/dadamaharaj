from rest_framework import viewsets, generics
from .models import Profile
from .serializers import ProfileSerializer
from django.shortcuts import render

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailByUsernameView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'  # use the 'username' field in the URL
# dadamaharaj/views.py

def profile_view(request, username):
    return render(request, "index.html", {"username": username})
