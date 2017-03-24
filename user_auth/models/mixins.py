from django.core.mail import send_mail


__all__ = ['EmailUserMixin', ]


class EmailUserMixin(object):

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])
