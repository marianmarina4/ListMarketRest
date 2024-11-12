from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self,instance, validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
    
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
    # Mostrar ciertos campos  (Para agregar un nuevo campo, actualizar .values en api)    
    def to_representation(self, instance):
        return {
            'id' : instance['id'],
            'username' : instance['username'],
            'email' : instance['email'],
            'password': instance['password']
        }
        
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')