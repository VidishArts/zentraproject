# users/views.py

from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import CustomUser, Interest, Message
from .serializers import UserSerializer, RegisterSerializer, InterestSerializer, MessageSerializer, LoginSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView

######################


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


#####################



class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



######################


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


#######################


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer


#######################


class InterestListView(generics.ListCreateAPIView):
    queryset = Interest.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = InterestSerializer


########################


class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MessageSerializer
