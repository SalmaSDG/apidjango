from django.shortcuts import render, get_object_or_404, redirect  
from django.http import JsonResponse
from django.core import serializers
from .models import Dataphone
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import DataphoneSerializer
from django.http import HttpResponse
#Importation des fonction d'authentification offerte par django
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

# myapp/views.py

from django.views.decorators.csrf import csrf_exempt
import json

class DataphoneDetail(APIView):
    def get(self,request):
        obj = Dataphone.objects.all()
        serializer = DataphoneSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer=DataphoneSerializer(data=request.data)
        if serializer.is_valid():
            imei = serializer.validated_data['imeiNumber']
            # Vérifiez si un enregistrement avec le même IMEI existe déjà
            if Dataphone.objects.filter(imeiNumber=imei).exists():
                return Response({"message": "IMEI déjà existant"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#fonction d'exportation des donnees sous format json
@login_required   #peut pas acceder a cette sans etre connecter
def export_data_to_json(request):
    data = serializers.serialize("json",Dataphone.objects.all())
    response = JsonResponse(data, safe=False)
    response['Content-Disposition'] = 'attachment; filename="data.json"'
    return response

#fonction exportation des donnees sous format scv
@login_required   #peut pas acceder a cette sans etre connecter
def export_data_to_csv(request):
    data = Dataphone.objects.all().values()  # Récupère les données sous forme de dictionnaires

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    # Écrit l'en-tête CSV
    header = data[0].keys()
    csv_data = ','.join(header) + '\n'

    # Écrit les données dans le fichier CSV
    for entry in data:
        csv_data += ','.join(str(entry[field]) for field in header) + '\n'

    response.content = csv_data.encode('utf-8')

    return response

#fonction affiche details
@login_required   #peut pas acceder a cette sans etre connecter
def show(request):
    student = Dataphone.objects.all()
    return render(request, 'show.html', {'student': student})
#fonction affiche des data stocke dans la base de donnee
@login_required   #peut pas acceder a cette sans etre connecter
def showData(request):
    student = Dataphone.objects.all()
    return render(request, 'dashboard.html', {'student': student})

@login_required   #peut pas acceder a cette sans etre connecter
def voirUser(request):
    student = User.objects.all()
    return render(request, 'utilisateur.html', {'student': student})

#fonction affiche home page
def home(request):
    return render(request, 'index.html')
#fonction affiche login page
#itadori1234
#satoru
#gojo
#satoru@gmail.com
#faissal
#issiaka1234
def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Bienvenue')
            return redirect('showData')
        else:
            messages.error(request, "erreur d'authentification")
    return render(request, 'login.html')
#fonction affiche register page
@login_required   #peut pas acceder a cette sans etre connecter
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription effectué avec succes")
            return redirect('voiruser')
        else:
            messages.error(request, form.errors)
    return render(request, 'register.html', {'form': form})
#Fonction de deconnexion
@login_required   #peut pas acceder a cette sans etre connecter
def deconnexion(request):
    logout(request)
    return redirect('home')