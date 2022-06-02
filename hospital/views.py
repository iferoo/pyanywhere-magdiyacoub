from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from knox.auth import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer

# from knox.auth import AuthToken
# from rest_framework import generics
# from .serializers import ChangePasswordSerializer
# from rest_framework.permissions import IsAuthenticated

# Create your views here.


class DoctorViews(APIView):
    def post(self, request):
        serializer = DoctorSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, id=None):
        if id != None:
            doctor = Doctor.objects.get(id=id)
            serializer = DoctorSerilizer(doctor)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            doctors = Doctor.objects.all()
            serializer = DoctorSerilizer(doctors, many=True)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

    def put(self, request, id=None):
        doctor = Doctor.objects.get(id=id)
        serializer = DoctorSerilizer(
            doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        doctor = get_object_or_404(Doctor, id=id)
        doctor.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class NurseViews(APIView):
    def post(self, request):
        serializer = NurseSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, id=None):
        if id != None:
            nurse = Nurse.objects.get(id=id)
            serializer = NurseSerilizer(nurse)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            nurses = Nurse.objects.all()
            serializer = NurseSerilizer(nurses, many=True)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

    def put(self, request, id=None):
        nurse = Nurse.objects.get(id=id)
        serializer = NurseSerilizer(
            nurse, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        nurse = get_object_or_404(Nurse, id=id)
        nurse.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class RoomViews(APIView):
    def post(self, request):
        serializer = RoomSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, id=None):
        if id != None:
            room = Room.objects.get(id=id)
            serializer = RoomSerilizer(room)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            rooms = Room.objects.all()
            serializer = RoomSerilizer(rooms, many=True)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

    def put(self, request, id=None):
        room = Room.objects.get(id=id)
        serializer = RoomSerilizer(
            room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        room = get_object_or_404(Room, id=id)
        room.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class BedViews(APIView):
    def post(self, request):
        serializer = BedSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, id=None):
        if id != None:
            bed = Bed.objects.get(id=id)
            serializer = BedSerilizer(bed)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            beds = Bed.objects.all()
            serializer = BedSerilizer(beds, many=True)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

    def put(self, request, id=None):
        bed = Bed.objects.get(id=id)
        serializer = BedSerilizer(
            bed, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        bed = get_object_or_404(Bed, id=id)
        bed.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class PatientViews(APIView):
    def post(self, request):
        serializer = PatientPostSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, id=None):
        if id != None:
            patient = Patient.objects.get(id=id)
            serializer = PatientSerilizer(patient)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            patients = Patient.objects.all()
            serializer = PatientSerilizer(patients, many=True)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

    def put(self, request, id=None):
        patient = Patient.objects.get(id=id)
        serializer = PatientPostSerilizer(
            patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        patient = get_object_or_404(Patient, id=id)
        patient.delete()
        return Response({"status": "success", "data": "Item Deleted"})


@api_view(['POST'])
def register_api(request):

    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        },
        'token': token
    })


@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        },
        'token': token
    })


@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'email': user.email,
                'is_superuser': user.is_superuser,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
            },
        })
    else:
        return Response({'error': 'not authenticated'}, status=400)
