from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel
# created 랑 modified 만들어줌 (created_at, updated_at)
from django.contrib.auth import get_user_model

# pip install pillow pilkit django-imagekit  # image 넣을 때 한세트처럼 사용할 것
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit


User = get_user_model()


class HashTag(TimeStampedModel):
    content = models.CharField(max_length=20, unique=True)  # 같은거 또 작성 못하게


class Posting(TimeStampedModel):
    like_users = models.ManyToManyField(User, related_name='like_posts')
    # posting 과 user 를 엮어준다
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postings')
    # 이름은 뭐라고 하든지 맘대로
    
    hashtags = models.ManyToManyField(HashTag, blank=True, related_name='postings')
    # 해시태그 없어도 되니까 blank True

    content = models.CharField(max_length=140)


    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse("postings:posting_detail", kwargs={"posting_id": self.pk})


class Image(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='images')  # related name 은 그냥 어떻게 부를지 정하는 것
    file = ProcessedImageField(
        # processors=[ResizeToFill(600, 600)],  # 크롭
        processors=[ResizeToFit(600, 600, mat_color=(45, 45, 45))],  # 알아서 비율 맞춰줌 
        upload_to='postings/images', 
        format='JPEG',
        options={'quality': 90},
    )


class Comment(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # User 가 comment 를 어떻게 부를까
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)



