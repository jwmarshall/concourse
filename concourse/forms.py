from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    tos = forms.BooleanField(
        label = _("Terms of Service"),
        required = True
    )
    privacy = forms.BooleanField(
        label = _("Privacy Policy"),
        required = True
    )
    username = forms.RegexField(
        label = _("Username"),
        max_length = 30,
        regex = r'^[\w_]+$',
        help_text = _("30 character limit, alphanumeric only."),
        error_messages = {
            'invalid': _("Invalid username. Alphanumeric characters only.")
        }
    )
    password2 = forms.CharField(
        label = _("Password confirmation"),
        widget = forms.PasswordInput,
        help_text=_("Enter the same password as above.")
    )

    class Meta:
        model = User
        fields = ("email","username","password1","password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

