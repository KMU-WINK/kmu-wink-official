from django.forms import ModelForm
from .models import Comment, Document


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        # 각 input 태그의 help_text, label을 제거함.
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
        self.fields['content'].widget.attrs['placeholder'] = "내용"



class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'content', 'image1', 'image2']

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)

        # 각 input 태그의 help_text, label을 제거함.
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
        self.fields['title'].widget.attrs['placeholder'] = "제목"
        self.fields['content'].widget.attrs['placeholder'] = "내용"
