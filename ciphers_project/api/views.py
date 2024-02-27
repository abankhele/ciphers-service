from django.http import JsonResponse
from .ciphers import caesar_enocde

def greetings(request):
    result={"message":"Welcome to ciphers service!"}
    return JsonResponse(result)

def encode(request,plaintext,shift):
    parameters=dict(request.GET)
    print(parameters)
    cipher=caesar_enocde(plaintext,shift)
    return JsonResponse({"cipher": cipher})
# Create your views here.
