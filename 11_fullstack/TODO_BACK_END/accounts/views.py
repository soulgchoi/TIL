from django.shortcuts import get_object_or_404

from rest_framework.response import Response  # JSON 응답 생성기
from rest_framework.decorators import api_view  # require_methods
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny  # 회원가입은 인증을 볼 필요가 없음

from .serializers import UserCreationSerializer, UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # user.set_password(request.data.get('password'))
        user.set_password(user.password)  # password 암호화
        # 암호화 안되면 token 발급이 안됨
        user.save()
        return Response(status=200, data={'message': '회원가입 성공'})


@api_view(['GET'])
def my_todos(request):
    user = request.user  # JWT 를 통해서, 요청보낸 사용자를 잡아냄
    serializer = UserSerializer(user)
    return Response(serializer.data)