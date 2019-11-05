from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm  # 가입 / 정보수정 / 로그인

# from .models import User
from django.contrib.auth import get_user_model  # 하나만 바꿔도 되는 코드!!
User = get_user_model()


class CustomUserCreationsForm(UserCreationForm):  # usercreationsform 상속받아서

    class Meta: # (UserCreationForm):
        model = User
        fields = ('username', 'email',)



class CustomAuthenticationForm(AuthenticationForm):
    class Meta:  # 뭔가 저장하는게 아닌 form
        model = User
