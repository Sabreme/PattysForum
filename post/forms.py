from django import forms

from .models import Post

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('message',)
        widgets = {
            'message': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }
