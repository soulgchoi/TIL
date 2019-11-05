from django.contrib import admin
from .models import Posting

class PostingModelAdmin(admin.ModelAdmin):
    # 시간이 함께 나오게 함
    readonly_fields = ('created_at', 'updated_at',)
    list_display = ('id', 'content', 'created_at', 'updated_at')
    list_display_links = ('id', 'content')

# 위에서 생성한 class 를 줘야 화면에 나타난다
admin.site.register(Posting, PostingModelAdmin)
