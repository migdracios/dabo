from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, nickname, password=None):
        if not username:
            raise ValueError('아이디를 입력해주세요')
        user = self.model(
            username=username,
            nickname=nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nickname, password=None):
        user = self.create_user(
            username=username,
            password=password,
            nickname=nickname
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField("사용자 아이디", max_length=20, unique=True)
    password = models.CharField("사용자 비밀번호", max_length=256)
    nickname = models.CharField("사용자 닉네임", max_length=20, unique=True)
    created_at = models.DateTimeField("사용자 계정 생성일자", auto_now_add=True)

    is_active = models.BooleanField("사용자 활성상태", default=True)
    is_admin = models.BooleanField("관리자 계정", default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nickname"]

    objects = UserManager()

    def __str__(self):
        return self.username
