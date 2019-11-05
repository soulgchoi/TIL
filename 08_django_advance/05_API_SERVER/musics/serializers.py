from rest_framework import serializers
from . models import Artist, Music, Comment


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)



class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)


class ArtistDetailSerializer(ArtistSerializer):
    # music 을 같이 보여주고 싶어서 위의 artistserializer 를 상속받음
    music_set = MusicSerializer(many=True)

    # class Meta:
    #     fields = ('id', 'name', 'music_set')
    # 왜 이렇게 쓰지 않을까?
    # 상속받은 class 가 바뀌어도 자동으로 바꾸기 위해
    # 최대한 코드상에 영향을 덜 받으려고


    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('music_set',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id',)


class MusicDetailSerializer(MusicSerializer):
    comments = CommentSerializer(source='comment_set', many=True)
    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comments',)
