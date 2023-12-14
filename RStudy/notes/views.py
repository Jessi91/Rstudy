from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(["GET"])
def sendData(request):
    dummy_dict = {
        "id" : 1,
        "name" : "jess"
    }

    return Response(dummy_dict)

