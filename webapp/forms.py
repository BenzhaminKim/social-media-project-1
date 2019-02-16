from .models import Post
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content',)
        widgets = {
            'content' : SummernoteWidget(),
        }
