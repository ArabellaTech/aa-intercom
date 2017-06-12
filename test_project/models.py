from django.contrib.auth.models import AbstractUser

from aa_intercom.mixins import IntercomUserMixin


class UserModel(AbstractUser, IntercomUserMixin):
    pass
