from django import forms
from .models import Comment, Blog

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        
        fields = ["comment"]  # we made a form to access the module forms that assist in validation , rather than manual validation

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        
        fields = ["title", "post", "name","description",
                  "image", "category"]
        
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Blog
        
        fields = ["title", "post", "description",
                  "image", "category"]