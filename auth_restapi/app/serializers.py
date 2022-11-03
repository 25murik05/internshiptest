from django.contrib.auth import authenticate
from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from .models import User


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(
        label="Login",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        login = attrs.get('login')
        password = attrs.get('password')

        if login and password:
            user = authenticate(request=self.context.get('request'),
                                login=login, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "login" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'login', 'password', 'phone', 'name', 'birth', 'tg', 'email',)
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'tg': {'required': False},
            'email': {'required': False},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
