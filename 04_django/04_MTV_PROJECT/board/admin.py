from django.contrib import admin
from .models import Article

# $ python manage.py migrate
# $ python manage.py createsuperuser
admin.site.register(Article)
