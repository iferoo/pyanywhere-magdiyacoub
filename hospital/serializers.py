from rest_framework import serializers, validators
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class PatientSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = "__all__"
        depth = 2


class PatientPostSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = "__all__"


class DoctorSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        depth = 1


class NurseSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Nurse
        fields = "__all__"
        depth = 1


class BedSerilizer(serializers.ModelSerializer):
    Patient = PatientSerilizer(read_only=True)

    class Meta:
        model = Bed
        # fields = ['id', 'Number', 'Status', 'Patient']
        fields = "__all__"
        # depth = 1


class RoomSerilizer(serializers.ModelSerializer):
    Beds = BedSerilizer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = "__all__"
        depth = 1


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name',
                  'last_name', 'is_superuser', 'is_active', 'is_staff')

        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with that Email already exists"
                    )
                ]
            },
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        is_superuser = validated_data.get('is_superuser')
        is_active = validated_data.get('is_active')
        is_staff = validated_data.get('is_staff')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_superuser=is_superuser,
            is_active=is_active,
            is_staff=is_staff
        )

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name',
                  'last_name', 'is_superuser', 'is_staff', 'is_active')

        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with that Email already exists"
                    )
                ]
            }
        }


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
