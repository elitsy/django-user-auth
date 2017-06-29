from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


__all__ = ['UserManager', 'EmailUserManager']


class UserManager(BaseUserManager):

    def prepare_fields_for_create(self, fields):
        """
        Default for django user auth by username
        """
        username = fields.get('username', False)
        if not username:
            raise ValueError('The given username must be set')
        fields['username'] = username

        email = fields.get('email', False)
        if email:
            email = UserManager.normalize_email(email)
            fields['email'] = UserManager.normalize_email(email)

        return fields

    def create_user(self, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        extra_fields = self.prepare_fields_for_create(extra_fields)
        user = self.model(is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **extra_fields):
        u = self.create_user(**extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class EmailUserManager(UserManager):

    def prepare_fields_for_create(self, fields):
        if 'email' in fields:
            email = UserManager.normalize_email(fields['email'])
            if not email:
                raise ValueError(_('The given email must be set'))
            fields['email'] = email
        if get_user_model().USERNAME_FIELD not in fields:
            raise ValueError('The `%s` field must be set' % \
                             get_user_model().USERNAME_FIELD)
        return fields