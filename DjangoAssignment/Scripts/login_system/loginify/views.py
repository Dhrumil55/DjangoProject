from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import User
from .serializers import UserSerializer
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def hello_world(request):
    return HttpResponse("hello world")

def hello_world_loginify(request):
    return render(request,'loginify/home.html')

@csrf_exempt
def all_data(request):
    if request.method == 'GET':
        try:
            all_data = User.objects.all() #we get data in the form of queryset
            serializer_data = UserSerializer(all_data,many=True)
            return JsonResponse(serializer_data.data,safe=False)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
    
    if request.method == 'POST':
        try:
            input_data = json.loads(request.body)
            serializer_data = UserSerializer(data=input_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({"message":"data saved succesfully"},status=201)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)

@csrf_exempt
def single_user_data(request,email):
    if request.method == 'GET':
        try:
            user_data = User.objects.get(email=email) #get single user data
            serializer_data = UserSerializer(user_data)
            return JsonResponse(serializer_data.data,status=200)
        except User.DoesNotExist:
            return JsonResponse({"error":"user not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
    if request.method == 'PUT':
        try:
            input_data = json.loads(request.body)
            user = User.objects.get(email=email)
            serializer_data = UserSerializer(user,data=input_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({"message":"data saved succesfully"},status=201)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except User.DoesNotExist:
            return JsonResponse({"error":"user not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)

    if request.method == 'DELETE':
        try:
            user_data = User.objects.get(email=email) #get single user data
            user_data.delete()
            return JsonResponse({"message":"data deleted succesfully"},status=204)
        except User.DoesNotExist:
            return JsonResponse({"error":"user not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)


    


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create(username=username, email=email, password=password)
        return redirect('login')
    return render(request,'loginify/signup.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email, password=password)
            return HttpResponse(f"Welcome, {user.username}!")
        except Exception as e:
            return HttpResponse("Invalid email or password.")
    return render(request, 'loginify/login.html')

