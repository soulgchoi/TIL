from django.db import models


class Student(models.Model):  # 클래스 상속
    # django 는 얻어걸리는걸 의도함(self X)
    # str, int 어떤 정보를 저장할지 자료형 지정
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    github_id = models.CharField(max_length=50)
    age = models.IntegerField()


class Menu(models.Model):
    # name : 메뉴이름 string
    # price : 가격 float? int?
    # category : 카테고리 string
    name = models.CharField(max_length=20)
    price = models.FloatField()
    category = models.CharField(max_length=10)
