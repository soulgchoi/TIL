from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),  # url 들어오면, obtain~~ 하겠다.
    path('api/v1/todos/', include('todos.urls')),
    path('api/v1/users/', include('accounts.urls')),
]
