from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

class CustomUserManager(BaseUserManager):
    def createMember(self, username, password):
        member = self.model(username=username)
        member.set_password(password)
        member.save()
        return member

#TODO: AbstractUser 동작원리 찾아보기
class User(AbstractUser):
    objects = CustomUserManager()

    class Meta:
        managed = True
        db_table = 'users'