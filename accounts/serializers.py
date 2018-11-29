from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import exceptions

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        username = data.get("username"," ")
        password = data.get("password"," ")

        if username and password:
            user = authenticate(username=username,password=password)
            if user.is_active:
                data["user"]= user
            else:
                msg = "kullanıcı aktif değil"
                raise exceptions.ValidationError(msg)   
        else:
            msg = "username and password yok"
            raise exceptions.ValidationError(msg)
            print("asdasdasdasdasd")
        return data
