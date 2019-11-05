from django.db import models


class HotIssue(models.Model):
    date = models.CharField(max_length=1024)
    time = models.CharField(max_length=1024)
    rank = models.IntegerField()
    keyword = models.CharField(max_length=1024)
