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
        
            name = request.GET.get('name', None)
            print(name)
            doctors={}
            if name is not None:
                
                doctors = DoctorModel.objects.filter(name=name)[0]
                for item in doctors:
                    print(item)
                   
                print('name',doctors)
            else:
                doctors = DoctorModel.objects.all()
                for item in doctors:
                    
                    print(item)
                    # for i in item:
                        # print(i['_id'])
                # print('all', list(doctors))
            
            doctors_serializar = DoctorSerializers(doctors, many=True)
            print(doctors_serializar)
            return JsonResponse(doctors_serializar.data, safe= False)
        except Exception as e:
            print(e)
            return JsonResponse(e)
    
    # def post(self, request):
    #     doctor = JSONParser().parse(request)
    #     print(doctor)
    #     doctor_serializer = DoctorSerializers(data=doctor)
    #     if doctor_serializer.is_valid():
    #         doctor_serializer.save()
    #         return JsonResponse(doctor_serializer.data, status=status.HTTP_201_CREATED)
    #     return JsonResponse(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
    def update(self, request):
        pass
    
    def delete(self, request):
        pass