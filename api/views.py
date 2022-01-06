from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from plep_app.models import Client
from .serializers import ClientSerializer


@api_view(['GET'])
def getClient(request, pk):
    client = Client.objects.get(uid=pk)
    serializer = ClientSerializer(client, many=False)
    return Response(serializer.data)
