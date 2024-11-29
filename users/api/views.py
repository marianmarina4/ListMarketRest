from rest_framework import status, generics
from rest_framework.response import Response
from users.models import User
from users.api.serializers import UserSerializer, UserListSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return User.objects.filter(id=pk)