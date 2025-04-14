from django.urls import path
from .views import ProfileListView, ProfileDetailByUsernameView

urlpatterns = [
    path('profiles/', ProfileListView.as_view(), name='profile-list'),
    path('profiles/<slug:username>/', ProfileDetailByUsernameView.as_view(), name='profile-detail'),
]
