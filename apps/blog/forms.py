from django import forms
from .models import Blog
# from django.contrib.auth.forms import BlogChangeForm
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'thumbnail_image')

class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'thumbnail_image')