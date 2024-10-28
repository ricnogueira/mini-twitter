""" from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer


class UserResigisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # user = serializer.validated_data['user']
        # user = serializer.save()
        # return Response({"user": user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
 """

# views.py
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserRegisterSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]  # Permite acesso sem autenticação

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["delete"], url_path="unregister")
    def delete(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response(
                {"message": "You must be logged in to perform this action."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        print(user)
        user.delete()  # Cancela a conta do usuário
        return Response(
            {"message": "Your account has been successfully cancelled!"},
            status=status.HTTP_204_NO_CONTENT,
        )
