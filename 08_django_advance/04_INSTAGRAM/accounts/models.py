from django.db import models
from django.urls import reverse
# User < AbstractUser < AbstractBaseUser / User 나 AbstratctUser 나 별 차이 없어서...
from django.contrib.auth.models import AbstractUser  # ctrl + 눌러서 model 확인해보기
from django.conf import settings
from faker import Faker
f = Faker()

class User(AbstractUser):  # 위에서 import 한 AbstractUser 상속
    fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars')  #, blank=True)
    # (User, related~~) 쓰고 migrate 해보면 User 못찾음
    # 'accounts.User' 혹은 self == settings.AUTH_USER_MODEL  # 변수처리 > settings 가서 바꾸면 끝


    def __str__(self):
        return self.username

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            u = cls()
            u.username = f.first_name()
            u.set_password('123qwe')
            u.save()
    # python manage.py shell_plus
    # User.dummy(n)  # 더미 데이터 만들기

    # 팔로우 추가해보기
    # star = User.objects.first()
    # fan1 = User.objects.last()
    # fan2 = User.objects.get(id=2)
    # star.fans.all()  # star 의 fans 보기
    # star.fans.add(fan1)  # star 의 fans 추가
    # star.fans.add(fan2)
    # star.stars.all()  # star 의 stars 확인
    # fan1.stars.all()  # fan1 의 stars 확인
    # fan2.start.all()

    # 내가 나를 팔로우 하는 것 막기

    def get_absolute_url(self):
        return reverse("accounts:user_page", kwargs={"user_id": self.pk})
    