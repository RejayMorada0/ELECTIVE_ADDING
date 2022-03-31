from django.db.models import fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import studentaccounts


class AuthorForm(ExtendedMetaModelForm):
    class Meta:
        model = Author
        field_args = {
            "email" : {
                "error_messages" : {
                    "required" : "Email already exist!"
                }
            }
        }