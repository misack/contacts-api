from rest_framework import serializers
# here we use/ import user for inheritance of user model
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=65,min_length=8, write_only=True)
    email=serializers.EmailField(max_length=65,min_length=8, write_only=True)
    first_name= serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta: #some information
        model=User
        # fields allowed for user to see
        fields = ['username', 'password','email', 'first_name', 'last_name']

    # override validate for validation, this method is called before date saved
    def validate(self, attrs):
        email = attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email is already in use')})

        return super().validate(attrs)

    # save data
    def create(self, validated_data):
        # return super().create(validated_data)
        # django way
        return User.objects.create_user(**validated_data)



# For swagger authorisation  
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password']




