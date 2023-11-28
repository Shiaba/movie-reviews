from .models import Comment, Review
from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'excerpt', 'category',
                  'rating', 'featured_image', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your review here'}),
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'excerpt': forms.TextInput(attrs={'placeholder': 'Add a short desccription'}),
        }
