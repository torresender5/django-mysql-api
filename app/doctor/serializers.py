

from rest_framework import serializers
from doctor.models import DoctorModel
class DoctorSerializers(serializers.ModelSerializer):
    
    class Meta:
        model= DoctorModel
        fields= ( 
            # '_id',
            # 'id',
            'name',
            'lastname',
            'office_address',
            'phone',
            'email'
        )