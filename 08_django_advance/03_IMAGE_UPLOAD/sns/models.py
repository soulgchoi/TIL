from django.db import models
from django.urls import reverse
from django.conf import settings  # MASTER_APP/settings.py
from faker import Faker
f = Faker()

# class Like(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Posting(models.Model):
    # 사용자 정보, 누구로부터 작성되었는지
    # auth ~~ 는 settings 에서 가져옴
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_postings', blank=True)
    # db 에 sns_posting_like_users 테이블이 생긴 것을 확인할 수 있다. (ManyToMany 가 만듦, migrate 할 때 생성)
    content = models.TextField()
    # 새로 column 을 추가 할 때, default 값이 없으면 메시지 출력
    icon = models.CharField(max_length=30, default='')
    # 메시지에서 선택해서 default 를 줄 수도 있지만, models 코드에서 괴리가 생기기 때문에
    # 직접 주는 것이 좋다.
    # view_count = models.IntegerField()
    # 지운 상태로 다시 makemigrations + migrate 가능

    # 테이블 지우는 방법
    # 1. 테이블을 주석처리하고 makemigrations + migrate
    #    => 데이터 삭제됨
    # 2. $ python manage.py migrate <APP_NAME> zero
    #    => applying 됐던 테이블이 unapplying 됨
    #    migrations 에 있는 파일 전부 삭제하면 새로 makemigrations 했을 때 0001 부터
    #    rm <APP_NAME>/migrations/0* ( 0으로 시작하는 것 전부 삭제 )
    #    python manage.py migrate zero 는 한번에 안됨 <APP_NAME> 필수
    

    image = models.ImageField(blank=True)  # 빈 값일 수도 있다, 여기서는 이미지가 없을 수도 있다
    # imagefield 는 db 에 image 가 "어디있는지" 저장하는 charfield 역할
    # image 없어도 된다고(black=True) 했는데 막상 안넣고 저장하면 html 에서 에러...
    # html 에서 if 문

    created_at = models.DateTimeField(auto_now_add=True)  # 처음 add 될 때 시간 들어가고 끝 (고정값)
    updated_at = models.DateTimeField(auto_now=True)  # 값이 바뀔 때 마다

    # views 에서 정렬해서 출력하지 않고, models 에서 아예 정렬
    class Meta:  # class Meta 가 있어야 정보에 관한 내용이라고 알 수 있음
        ordering = ['-created_at',]  # created_at 을 내림차순(-)으로
    # 대신 데이터를 꺼낼 때마다, 무조건 이 기준

    # detail 페이지를 쓸거라면 만들기
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})

    
    # 객체가 str 으로 표시되게...
    def __str__(self):
        return f'{self.pk}: {self.content[:20]}'

    # python manage.py migrate 로 모든 app 을 migration 하면 superuser 를 만들 수 있음
    # python manage.py createsuperuser

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            cls.objects.create(
                user_id=1,
                content=f.sentence(),
                icon='fas fa-angrycreative',
            )

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    # related_name 이제부터 posting 이 comment 를 부를 때, comments 라고 부르자
    # 없으면 posting.comment_set 이 default / 있으면 posting.comments 로 
    content = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created_at',]


    @classmethod
    def dummy(cls, n, posting_id):
        for _ in range(n):
            cls.objects.create(
                user_id=1,
                posting_id=posting_id,
                content=f.sentence(),
            )


    def __str__(self):
        return f'{self.id}: {self.content[:10]}'
    
    
# shell plus 열고,
# Posting.dummy(10)
# Comment.dummy(10, 1)
# Posting.objects.first()
# Posting.objects.last()
# p = Posting.objects.last()
# u1 = User.objects.last()
# u2 = User.objects.first()
# 포스팅 하나와 두 명의 유저 저장
# Posting 에는 like_users 라는 값이 있음
# p.like_users.all()  > p 를 좋아하는 모든 유저들
# p.like_users.add(u1)  > p 를 좋아하는 유저 u1 이 추가됨, 중복은 불가
# u2.like_postings.add(p) 가 가능한 이유 > related name
# u2.like_postings.remove(p) > 좋아요 취소


# for i in range(10):
#     u = User()
#     u.username = f'dummyUser-no.{i}'
#     u.set_password('req123')  # password 암호화
#     u.save()