from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


from .manager import UserManager
from .validators import validate_tg, validate_birth


class User(AbstractBaseUser, PermissionsMixin):
    login_validator = UnicodeUsernameValidator()

    phone = PhoneNumberField(unique=True)
    login = models.CharField("login", max_length=150, unique=True, validators=[login_validator])
    name = models.CharField("name", max_length=150)
    birth = models.DateField("birthday", validators=[validate_birth])
    tg = models.CharField("telegram", max_length=64, blank=True, validators=[validate_tg])
    email = models.EmailField("email address", blank=True)
    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField("active", default=True,)
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['phone', 'name', 'birth']

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"Login: {self.login}, Phone: {self.phone}, Name: {self.name}, Birthday: {self.birth}"
