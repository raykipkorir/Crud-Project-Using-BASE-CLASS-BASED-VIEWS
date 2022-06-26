from django import forms
from .models import User

class AddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name',"last_name","email","password"]
        widgets = {
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"placeholder":"Enter Password","class":"form-control"}),
            "email":forms.EmailInput(attrs={"placeholder":"example@gmail.com","class":"form-control"})
        }
        labels = {"email":"E-mail"}
        help_texts = {"password":"Enter strong password"}

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("Email should end with edu")
