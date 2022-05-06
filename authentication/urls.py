from django.urls import path
from authentication.views import LoginAPI, UserLogoutAPIView

urlpatterns = [
    path('login/', LoginAPI.as_view(), name="login"),
    path('logout/', UserLogoutAPIView.as_view(), name="logout"),
]
