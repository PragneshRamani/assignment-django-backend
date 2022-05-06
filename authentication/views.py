from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


class LoginAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': username},
                        status=HTTP_200_OK)

class UserLogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):        
        try:
            request.user.auth_token.delete()            
            logout(request)
            return Response({
                "status": True,
                "code" : HTTP_200_OK,
                "message" : "Logout success.",       
                "result": {},
            }, status=HTTP_200_OK)
        #except 
        except Exception as e:
            return Response({
                "status": False,
                "code" : HTTP_400_BAD_REQUEST,
                "message" : "Unauthorised user",       
                "result": {},
            }, status=HTTP_400_BAD_REQUEST)