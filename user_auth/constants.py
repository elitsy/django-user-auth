# coding: utf-8
from django.utils.translation import ugettext_lazy as _

USER_GENDER_MALE = 1
USER_GENDER_FEMALE = 2

USER_GENDER_CHOICES = (
    (USER_GENDER_MALE, _(u'Мужской')),
    (USER_GENDER_FEMALE, _(u'Женский')),
)
