"""
User Model.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

"""User Model Manager"""


class UserManager(BaseUserManager):
    """Managers for users"""

    def create_user(self, email, password=None, **extra_fields):
        """ "Create, Save and Return user"""
        user = self.model(email=email, **extra_fields)
        # hash password
        user.set_password(password)
        # saving user, using part is for supporting multiple database if
        # needed.
        user.save(using=self._db)

        return user


"""User Model"""


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # this is for identifying is the user login as admin
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # means we will use email for authentication not name
    USERNAME_FIELD = "email"
