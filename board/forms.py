from django.forms import ModelForm
from .models import Comment, Document


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'content']
