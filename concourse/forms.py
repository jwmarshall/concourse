import re
from django import forms
from django.contrib.auth.models import User
from registration.forms import RegistrationForm
from django.utils.translation import ugettext, ugettext_lazy as _

class ConcourseRegistrationForm(RegistrationForm):
    default_widget_class = 'input-block-level'

    error_messages = { 
        'duplicate_username': _("Username has already been registered."),
        'password_mismatch': _("Password fields must match.")
    }

    username = forms.RegexField(
        label = _("Username"), 
        max_length = 30,
        regex = r'^[\w_]+$',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class': default_widget_class,
                'placeholder': _("30 character limit, alphanumeric only.")
            }
        ),
        error_messages = {
            'invalid': _("Invalid username. Alphanumeric characters only.")
        }
    )
    email = forms.EmailField(
        label = _("Email"),
        required = True,
        max_length = 75,
        widget = forms.TextInput(attrs={'class': default_widget_class}),
        error_messages = {
            'invalid': _("Invalid email address.")
        }
    )
    password1 = forms.CharField(
        label = _("Password"), 
        widget = forms.PasswordInput(
            attrs = {
                'class': default_widget_class,
                'placeholder': _("Uppercase, lowercase, and a number.")
            },
            render_value=False
        )
    )
    password2 = forms.CharField(
        label = _("Password Confirmation"),
        widget = forms.PasswordInput(
            attrs = {
                'class': default_widget_class,
                'placeholder': _("Enter the same password as above."),
            },
            render_value=False
        )
    )
    tos = forms.BooleanField(
        label = _("Terms of Service"),
        required = True,
        widget = forms.CheckboxInput(attrs={'class': default_widget_class}),
        help_text = _("I have read and agree to the Terms of Service")
    )

    class Meta:
        model = User
        fields = ("email","username","password1","password2")

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters.')
        elif not re.findall(r'[A-Z]', password):
            raise forms.ValidationError('Password must have an uppercase letter.')
        elif not re.findall(r'[a-z]', password):
            raise forms.ValidationError('Password must have a lowercase letter.')
        elif not re.findall(r'[0-9]', password):
            raise forms.ValidationError('Password must have a number.')
        return password

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError('Email address has already been registered.')
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

