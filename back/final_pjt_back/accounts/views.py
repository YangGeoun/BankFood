import random
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .form import CostomUserCreationForm
from .serializer import UserSerializer

# Create your views here.
@api_view(['POST'])
def signup(request):
    User = get_user_model()
    form = CostomUserCreationForm(data=request.data)
    if form.is_valid():
        form.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def userinfo(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)










#---------------------------------------------------------------------------------------#

first_name_samples = "김이박최정강조윤장임양부"
middle_name_samples = "민서예지도하주윤채현지건수"
last_name_samples = "준윤우원호후서연아은진환"

def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result + str(random.randint(1000, 9999))

username_list = []
N = 10000
i = 0

while i < N:
    rn = random_name()
    if rn in username_list:
        continue
    
    username_list.append(rn)
    i += 1

    
@api_view(['GET'])
def dummy(request):
    User = get_user_model()
    for i in range(N):
        user = User()
        user.nickname = username_list[i]
        user.username = username_list[i]
        user.age = random.randint(1, 100)  # 나이
        user.money = random.randrange(0, 1000000000, 1000000)   # 현재 가진 금액
        user.salary = random.randrange(0, 150000000, 100000) # 연봉
        user.password = "1234"
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.gender = random.choice([True, False])
        user.save()

    return Response({'asd':'as'})
    