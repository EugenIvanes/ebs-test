from copy import deepcopy
from django.contrib.auth.models import User
from rest_framework import status

from drf_util.decorators import serialize_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.users.serializers import (UserSerializer)


# Create your views here.

class RegisterUserView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(UserSerializer)
    def post(self, request):
        user_load = deepcopy(request.data)
        serializer = UserSerializer(data=user_load)
        serializer.is_valid()
        data = serializer.data
        user = User.objects.create(first_name=data.get('first_name'),
                                   last_name=data.get('last_name'),
                                   email=data.get('email'),
                                   username=data.get('username'))
        user.set_password(user_load['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
