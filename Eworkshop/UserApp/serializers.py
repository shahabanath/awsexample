from rest_framework import serializers
from UserApp.models import User, insurance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class insuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = insurance
        fields = '__all__'