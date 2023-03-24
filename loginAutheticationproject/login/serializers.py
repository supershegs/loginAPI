from rest_framework import serializers
from django.contrib.auth import get_user_model


#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = '__all__'
    #fields = ["id", "first_name", "last_name", "username"]