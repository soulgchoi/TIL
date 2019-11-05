from django.db import models
from django.urls import reverse


class Article(models.Model):
    # id 안넣는 이유, 무조건 생성되게 되어있어서
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 아래는 모두 ORM 에게 확인을 요청하는 과정
    # python manage.py makemigrations board
    # migrations 에서 확인
    # python manage.py sqlmigrate board 0001  > sql 에서 어떤건지 확인
    # python manage.py migrate board 라고 치면 db 에서 생성 및 확인 가능

    # python manage.py shell_plus
    # article = Article()
    # article.title = '안녕'
    # article.content = '안녕안녕'
    # article.save()   == INSERT INTO
    # save가 가능한 이유는 model에 내장되어 있기 때문
    # SELECT * FROM Article == Article.objects.all()
    # SELECT * FROM board.article WHERE id=1
    # == Article.objects.get(id=1)

    # python manage.py shell_plus --print-sql
    # python 코드를 sql 로 번역

    # DELETE FROM board_article WHERE id=1
    # == article = Article.objects.get(id=1) 변수 잡아놓고 삭제
    # article.delete()

    # Article.objects.create(title='hi', content='hihi')
    # 생성

    # python manage.py dbshell > sql 직접 접근

    # article = Article.objects.get(id=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    # method 생성
    # DB 에 반영안됨
    # detail 페이지가 있는 경우
    # detail 페이지를 자주 보니까, 절대 주소를 정의해놓고 다른 함수에서 'board:detail' 안써도 되도록
    def get_absolute_url(self):
        return reverse("board:article_detail", kwargs={"article_id": self.id})


class Comment(models.Model):
    # charfield 는 max_length 필수
    # 200 넘어가면 자름
    content = models.CharField(max_length=200)
    # foreignkey 는 integer 는 아니지만, 대충 Article 을 참조해서 id 를 가져오겠다는 의미
    # CASCADE 는 게시글을 삭제했을 때 종속된 것도 지워버림
    # 1:N 관계에서 필수
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # Article 변수를 가져왔기 때문에 class Article 과 순서 바꿀 수 없다.

    # 만들고 다시 migrate

    # c2 = Comment.objects.create(content='엥', article_id=3)
    # Article.objects.get(id=c2.article_id) == c2.article
    #    > comment 에게 article 이 있기 때문에 가능
    # == article.comment_set.all()
    # foreignkey 로 관계 형성!

    # 이제 views.py 의 detail 에 댓글 만들 것

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
