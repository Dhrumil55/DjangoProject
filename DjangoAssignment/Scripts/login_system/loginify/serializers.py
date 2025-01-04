from rest_framework import serializers
from .models import User
#normal
# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=50)
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=12)

#model serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"