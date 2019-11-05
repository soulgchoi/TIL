from django.db import models


class Artist(models.Model):
    name = models.TextField()
    

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)
    title = models.TextField()


class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.TextField()


# No search table error > 대부분 migrate 안한 문제