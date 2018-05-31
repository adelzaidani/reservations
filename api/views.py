from django.shortcuts import render
from reservations.models import Shows
from rest_framework import views, viewsets, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import ShowsSerializer
import requests

class ShowsList(APIView):

    def get(self,request):
        shows = Shows.objects.all()
        serializer = ShowsSerializer(shows,many=True)
        return Response(serializer.data)

class ShowsListById(APIView):

    def get(self, request, id_show):
        show = Shows.objects.get(id=id_show)
        serializer = ShowsSerializer(show, many=False)
        return Response(serializer.data)

def listefilms(request):
    response=requests.get('https://swapi.co/api/films/')
    films=response.json()
    titres=films["title"]
    return render(request,'api/liste_films.html',{films:'films'})

def testapi(request):
    return render(request,'api/test_api.html')

def api_google(request):
    return render(request,'api/api_google.html')



