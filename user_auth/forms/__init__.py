from .mixins import PasswordFormMixin, ChangePasswordMixin
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


__all__ = ['UserChangeForm', 'UserCreationForm']


class UserChangeForm(PasswordFormMixin):

    class Meta:
        model = get_user_model()
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.using('default').select_related('content_type')


class UserCreationForm(ChangePasswordMixin):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    class Meta:
        model = get_user_model()
        fields = [get_user_model().USERNAME_FIELD, ] + \
                    get_user_model().REQUIRED_FIELDS

    def clean_email(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"].strip()
        try:
            get_user_model().objects.using('default').get(email__iexact=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
