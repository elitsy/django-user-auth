# coding: utf-8

import re

from django.contrib import auth
from django.contrib.auth.models import Group
from django.core import validators
from django.core.validators import EMPTY_VALUES
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..constants import USER_GENDER_CHOICES, USER_GENDER_MALE, \
    USER_GENDER_FEMALE
from .mixins import EmailUserMixin


class DjangoAdmin(models.Model):
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    class Meta:
        abstract = True


class WithShortName(models.Model):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    class Meta:
        abstract = True

    def get_short_name(self):
        "Returns the short name for the user."
        return (u'%s %s' % (self.first_name, self.last_name)).strip()
    get_short_name.short_description = u'Имя'
    get_short_name.admin_order_field = 'first_name'
    short_name = property(get_short_name)


class WithFullName(WithShortName):
    middle_name = models.CharField(u'отчество', max_length=30,
                                   blank=True, null=True)

    class Meta:
        abstract = True

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = []
        if self.first_name not in EMPTY_VALUES:
            full_name.append(self.first_name)
        if self.middle_name not in EMPTY_VALUES:
            full_name.append(self.middle_name)
        if self.last_name not in EMPTY_VALUES:
            full_name.append(self.last_name)
        return u' '.join(full_name)
    get_full_name.short_description = u'ФИО'
    get_full_name.admin_order_field = 'first_name'

    full_name = property(get_full_name)


class WithEmail(EmailUserMixin, models.Model):
    email = models.EmailField(_('email address'), blank=True)

    class Meta:
        abstract = True


class WithUniqueEmail(EmailUserMixin, models.Model):
    email = models.EmailField(_('email address'), blank=True, unique=True)

    class Meta:
        abstract = True


class WithGroups(models.Model):
    groups = models.ManyToManyField(Group, verbose_name=_('groups'),
        related_name='%(class)ss', blank=True,
        help_text=_('The groups this user belongs to. A user will '
                                'get all permissions granted to each of '
                                'his/her group.'))

    class Meta:
        abstract = True

    def get_group_permissions(self, obj=None):
        """
        Returns a list of permission strings that this user has through his/her
        groups. This method queries all available auth backends. If an object
        is passed in, only permissions matching this object are returned.
        """
        permissions = set()
        for backend in auth.get_backends():
            if hasattr(backend, "get_group_permissions"):
                if obj is not None:
                    permissions.update(backend.get_group_permissions(self,
                                                                     obj))
                else:
                    permissions.update(backend.get_group_permissions(self))
        return permissions


class WithUsername(models.Model):
    username = models.CharField(_('username'), max_length=254, unique=True,
        help_text=_('Required. 254 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                      _('Enter a valid username.'), 'invalid')
        ])

    class Meta:
        abstract = True


class WithMobile(models.Model):
    mobile = models.CharField(_('mobile'), max_length=11, blank=True)

    class Meta:
        abstract = True


class WithGender(models.Model):
    GENDER_MALE = USER_GENDER_MALE
    GENDER_FEMALE = USER_GENDER_FEMALE

    GENDER_CHOICES = USER_GENDER_CHOICES

    gender = models.IntegerField(blank=True, null=True, choices=GENDER_CHOICES,
                                 default=None)

    class Meta:
        abstract = True
