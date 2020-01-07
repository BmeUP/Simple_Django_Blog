from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Post


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "email",
        )


class PostCreate(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
   # title = forms.CharField(max_length=100, widget=forms.TextInput, label="Title")
   # content = forms.CharField(max_length=100, widget=forms.Textarea, label="Content")
