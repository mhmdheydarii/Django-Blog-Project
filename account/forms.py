from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = ""
        self.fields["email"].widget.attrs["class"] = ""
        self.fields["password1"].widget.attrs["class"] = ""
        self.fields["password2"].widget.attrs["class"] = ""
        self.fields["username"].widget.attrs["placeholder"] = "Your Username"
        self.fields["email"].widget.attrs["placeholder"] = "Your Email"
        self.fields["password1"].widget.attrs["placeholder"] = "Your Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Repit Password"

