from django.shortcuts import render
from django.http import JsonResponse 
from django.views import View
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import DoctorModel 
from .serializers import DoctorSerializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json 
# Create your views here.

class DoctorView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get(self, request):
        try:
            doctors = DoctorModel.objects.all().values()
            print(doctors)
            dat= {}
            for i in doctors:
                # print(n)
                # for i in n: 
                #     print(i)
                dat=dict(
                    name=i.name,
                    lastname=i.lastname,
                    office_address=i.office_address,
                    phone=i.phone,
                    email=i.email
                )
            print(dat)
            doctors_serializers = DoctorSerializers(data=dat, many=True)
            print(doctors_serializers)
            # if doctors_serializers.is_valid():
            return JsonResponse(doctors_serializers.data, safe=False)
            # return JsonResponse({'message':'not found'})
        except Exception as e:
            print(e)
            return JsonResponse(e)
    
    def post(self, request):
        doctor = JSONParser().parse(request)
        print(doctor)
        doctor_serializer = DoctorSerializers(data=doctor)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse(doctor_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
    def update(self, request):
        pass
    
    def delete(self, request):
        pass