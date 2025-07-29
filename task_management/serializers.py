
from rest_framework import serializers
from .models import User  , TaskModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"

