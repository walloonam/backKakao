from django.db import IntegrityError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
import json
from .models import User


@csrf_exempt
@csrf_exempt
def user_signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        print(name)
        try:
            user = User(
                name=name,
                email=email,
                password=password
            )
            user.save()
            return JsonResponse({'message': 'User created successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def user_login(request):
    timezone.deactivate()
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            # 데이터 유효성 검사
            email = data.get('email')
            password = data.get('password')

            if not (email and password):
                return JsonResponse({'error': 'Name and password are required'}, status=400)

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': 'User logged in successfully'})
            else:
                return JsonResponse({'error': 'Invalid username or password'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)