from rest_framework import serializers 
from .models import*
from django.contrib.auth import get_user_model
from .utils import generate_activation_code, send_activation_email

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, read_only=True)
    password_confirm = serializers.CharField(min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password_confirm']

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('passwords must match!')
        return validated_data

    def create(self, validated_data):
        email = validated_data.get('email')
        name = validated_data.get('name')
        password = validated_data.get('password')
        print(f'PASSSWORD: {password}')
        user = User.objects.create_user(email=email, name=name, password=password)
        activation_code = generate_activation_code()
        user.activation_code = activation_code
        print('activation_code: ', activation_code)
        send_activation_email(email=email, activation_code=activation_code, action='register')
        user.save()
        return user
