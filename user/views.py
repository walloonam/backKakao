from django.db import IntegrityError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
import json
from django.views.decorators.http import require_GET

from app.models import ShowModel
from .models import User, Reserve, Like


@csrf_exempt
def user_signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')

            if not name:
                return JsonResponse({'error': 'Name field is required'}, status=400)
            if not email:
                return JsonResponse({'error': 'Email field is required'}, status=400)
            if not password:
                return JsonResponse({'error': 'Password field is required'}, status=400)
            if data.get('admin'):
                admin = True
            else:
                admin = False

            user = User(
                name=name,
                email=email,
                password=password,
                admin=admin
            )
            print("hi")

            user.save()
            print("hi")
            return JsonResponse({'message': 'User created successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
        except IntegrityError:
            return JsonResponse({'error': 'User with this email already exists'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if not (email and password):
                return JsonResponse({'error': 'Email and password are required'}, status=400)
            
            user = User.objects.get(email=email)
            if user is not None:
                return JsonResponse({'success': 'User logged in successfully'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid email or password'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@require_GET
def user_info(request, id):
    try:
        user = User.objects.get(id=id)
        user_data = {
            "message": "success",
            "email": user.email,
            "name": user.name,
            "reserve": [],
            "like": []
        }

        #여기는 하경이한테 줘야할 정보 보고 주기
        
        reservations = Reserve.objects.filter(email=user.email)
        for reservation in reservations:
            consert=ShowModel.objects.filter(title=reservation.consert)
            user_data["reserve"].append(consert)
        
        likes = Like.objects.filter(email=user.email)
        for like in likes:
            consert=ShowModel.objects.filter(title=like.consert)
            user_data["like"].append(consert)

        return JsonResponse(user_data)
    except User.DoesNotExist:
        return JsonResponse({"message": "fail"})
