from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse("board:article_detail", kwargs={"article_id": self.pk})
    