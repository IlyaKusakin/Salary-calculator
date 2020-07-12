from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import Inquiry
from django.contrib.auth.models import User
from django.utils import timezone

# import folder with util functions
import sys
sys.path.append(sys.path[0]+'/api/util_function')
from model_pred import model_prediction
# sys.path.insert(1, 'util_functions')
# sys.path.insert(3, '../')
# from predict import predictor
# from parsing import parser


# Inquiry
class InquiryDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Inquiry
        fields = "__all__"


class InquiryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        inquiry = Inquiry()
        inquiry.title = validated_data['title']
        inquiry.text = validated_data['text']
        inquiry.company = validated_data['company']
        inquiry.employment = validated_data['employment']
        inquiry.worktime = validated_data['worktime']
        inquiry.exp = validated_data['exp']
        inquiry.skills =validated_data['skills']
        inquiry.result = model_prediction(
                    inquiry.title, 
                    inquiry.company,
                    inquiry.employment,
                    inquiry.worktime,
                    inquiry.exp,
                    inquiry.skills,
                    inquiry.text)
    
        inquiry.user = validated_data['user']
        inquiry.save()
        return inquiry

    class Meta:
        model = Inquiry
        fields = "__all__"
       
        





class InquiryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = "__all__"




# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
