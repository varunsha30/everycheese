from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import TextField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(
        _("Name of User:"), blank=True, max_length=255, help_text="Full Name",
    )

    bio = models.TextField(_("Bio:"), blank=True, help_text="Enter your Bio baby :P")

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )
