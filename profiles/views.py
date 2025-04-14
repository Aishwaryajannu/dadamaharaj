from rest_framework import viewsets, generics
from .models import Profile
from .serializers import ProfileSerializer

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailByUsernameView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'  # use the 'username' field in the URL
