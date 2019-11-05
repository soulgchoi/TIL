from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST


@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/article_list.html', {
        'aritcles': articles,
    })