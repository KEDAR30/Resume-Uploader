from rest_framework import serializers 
from api.models import Profile

class ProfileSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['name','email','dob','state','gender','location','pimage','rdoc']
