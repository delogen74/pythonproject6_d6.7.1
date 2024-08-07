from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('NW', 'Новость'),
        ('AR', 'Статья'),
    ]
    categoryType = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Тип поста')

    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'postCategory', 'categoryType']
        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
            'image': 'Изображение',
            'postCategory': 'Категория',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Комментарий',
        }
