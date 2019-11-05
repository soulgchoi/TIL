from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Artist, Music

# forms 랑 유사하게 사용
from .serializers import ArtistSerializer, MusicSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer
from IPython import embed
from rest_framework.decorators import api_view
# django 보다 업그레이드 된 response 객체
from rest_framework.response import Response

# json 을 text 로 보내야 함
import json


# 달라    써라    수정      삭제
# GET    POST    PATCH    DELETE
# read   create  update   delete


@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    # data 가 여러개

    # embed()
    # artists
    # artist
    # serializer
    # s = artistserializer

    # 이게 기본 직렬화, 힘들어서 rest_framework 가 만들어진 것임
    # dataset = []
    # for artist in artists:
    #     d = {
    #         "id": artist.id,
    #         "name": artist.name
    #     }
    #     dataset.append(d)
    # # 웹 세상의 공용어로 바꾸기
    # # Serialization (직렬화)
    # res_data = json.dumps(dataset)
    # # print(type(res_data), res_data)
    # # class str
    # # 직렬화 = string 으로 바꿔줌

    # return HttpResponse(res_data)
    # return HttpResponse(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    # serializer = MusicSerializer(music)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)


@api_view(['POST'])
def create_comment(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    serializer = CommentSerializer(data=request.data)  # request.POST vs. request.data
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music.id)  # 저장완료
    return Response(serializer.data)  # 저장한 데이터