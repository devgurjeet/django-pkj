from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    data = {"message": "It Worked."}
    return JsonResponse(data)
