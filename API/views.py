from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Alumno, Carrera
from .serializers import AlumnoSerializer, CarreraSerializer

# Método de login
@api_view(['POST'])
def login(request):
    username = request.data.get('nombre')
    password = request.data.get('contraseña')
    user = authenticate(username=username, password=password)
    if user is not None:
        return Response({"message": "Login exitoso"}, status=status.HTTP_200_OK)
    return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

# Método para agregar una carrera
@api_view(['POST'])
def add_carrera(request):
    serializer = CarreraSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Método para agregar un alumno
@api_view(['POST'])
def add_alumno(request):
    serializer = AlumnoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)