from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # 생성할 때 자동으로
    modified = models.DateTimeField(auto_now=True)  # 변경될 때마다 자동으로 갱신

    def __str__(self):
        return f'{self.id}: {self.title}'
        