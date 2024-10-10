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
        
    
        
        
        
# class TestUserSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 200)
#     email = serializers.EmailField()
    
#     def validate_name(self, value):
#         # validation
#         if 'develop' in value:
#             raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')
        
#         return value
    
#     def validate_email(self, value):
#         # validation
#         if value == '':
#             raise serializers.ValidationError('Tiene que indicar un correo')

#         if self.validate_name(self.context['name']) in value :
#             raise serializers.ValidationError('El email no puede contener el nombre')
        
#         return value
    
#     # is_valid() llama esta función
#     def validate(self, data):
#         return data
    
#     # save() llama a esta función si no se le pasa una instancia
#     def create(self, validated_data):
#         return self.model.objects.create(**validated_data)
    
#     # save() llama a esta funcion si recibe una instancia
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance
