from .serializers import InquiryDetailSerializer, InquiryListSerializer, InquiryCreateSerializer
from .serializers import UserSerializer
from .models import Inquiry
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from django.http import FileResponse
from django.core.files import File

import sys
sys.path.append(sys.path[0]+'/api/util_function')
from model_pred import model_prediction


# Inquiry
class InquiryCreateViewAuth(generics.CreateAPIView):
    serializer_class = InquiryCreateSerializer
    permission_classes = (IsAuthenticated,)

class InquiryCreateView(APIView):
    permission_classes = ()

    def post(self, request, ):
        try:   
            return Response({
                "result":model_prediction(
                    request.data.get("title"), 
                    request.data.get("company"),
                    request.data.get("employment"),
                    request.data.get("worktime"),
                    request.data.get("exp"),
                    request.data.get("skills"),
                    request.data.get("text")
                )
                })
        except:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)



class GetInquiriesView(generics.ListAPIView):
    serializer_class = InquiryListSerializer
    queryset = Inquiry.objects.all()
    permission_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        return Inquiry.objects.filter(user_id=self.request.user)


class InquiryDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = InquiryDetailSerializer
    queryset = Inquiry.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


#Auth
class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request, ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response(
                {"token": user.auth_token.key, "id_user": user.id, 'email': user.email, 'username': username})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
