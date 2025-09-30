from django import forms
from .models import UserAccount

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ["username", "role_id", "description", "blocked"]
