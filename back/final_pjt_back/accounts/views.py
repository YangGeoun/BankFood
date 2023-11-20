from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .form import CostomUserCreationForm

# Create your views here.
@api_view(['POST'])
def signup(request):
    User = get_user_model()
    form = CostomUserCreationForm(data=request.POST)
    if form.is_valid():
        form.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

def test(request):
    form =CostomUserCreationForm
    context = {
        'form' : form 
    }
    return render(request,'index.html',context)