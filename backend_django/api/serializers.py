from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, style={"input_type": "password"})
  class Meta:
    model  = User
    fields = ["id", "username", "password"]
    extra_kwargs = {"password": {"write_only": True}}

  def create(self, data):
    user = User.objects.create_user(**data)
    return user