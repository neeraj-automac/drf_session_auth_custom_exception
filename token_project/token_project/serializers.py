from .models import *
from rest_framework import serializers


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(error_messages={
        'blank': ' password_field_cannot_be_blank.'
    })

    email = serializers.CharField(error_messages={
        'blank': 'username_field_cannot_be_blank.'
    })



    class Meta:
            model = User
            fields = ('email', 'password')
