from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import  *
from django.contrib.auth.models import User
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password':{'write_only':True}}

#         def create(self, validated_data):
#             user = User(
#                 email=validated_data['email'],
#                 username = validated_data['username'],
#             )
#             user.set_password(validated_data['password'])
#             user.save()
#             Token.objects.create(user=user)
#             return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name','email')
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active',)

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class AccountUserSerializer(serializers.ModelSerializer):
	class Meta:
	    model = AccountUser
	    fields = '__all__'

