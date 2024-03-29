
from django import forms
from .models import SupportTicket, Contact
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import  User

class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['subject', 'description', 'status']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']



# class CustomSupportUserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields.pop('password2')
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['email', 'password1']

