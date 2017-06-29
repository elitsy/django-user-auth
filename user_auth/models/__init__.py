from .managers import EmailUserManager
from .parts import DjangoAdmin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


__all__ = ['AbstractUser']


class AbstractUser(DjangoAdmin, AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    If you use mixins or other models to extend your user class, it must be
    placed at the end of them
    """
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = EmailUserManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True

    username = property(AbstractBaseUser.get_username)
