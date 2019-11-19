from django.shortcuts import get_object_or_404

from rest_framework.response import Response  # JSON 응답 생성기
from rest_framework.decorators import api_view  # require_methods

from .models import Todo
from .serializers import TodoSerializer


# @api_view(['GET'])
# def todo_list(request):
#     serializer = TodoSerializer


@api_view(['POST'])
def create_todo(request):
    # serializer = TodoSerializer(data=request.POST)  # request.POST > form-data 만 잡음
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        # serializer.data > { 'id': 1, 'user_id': 1, 'title': '따쉬', 'completed': false }
        return Response(serializer.data)
    # error = {
    #     'message': 'Invalid Todo',
    # }
    # return Response(status=400, data=error)
    return Response(status=400, data=serializer.errors)
    # POST 방식으로, /todos/, headers 에 JWT + token, body 에 user id
    # > payload


@api_view(['PATCH', 'DELETE'])
def update_delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)

    if request.method == 'PATCH':
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=400, data=serializer.errors)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=204)