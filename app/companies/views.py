from django.shortcuts import render
from django.views import View
from django.http import JsonResponse 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json 

# Create your views here.
class Company(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        jd= json.loads(request.body)
        
        return JsonResponse(jd)
    
    def post(self, request):
        pass 
    
    
    def put(self, request):
        pass 
    
    def update(self, request):
        pass 
    
