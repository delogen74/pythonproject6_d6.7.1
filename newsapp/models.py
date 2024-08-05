# newsapp/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.validators import MinValueValidator

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating') or 0

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating') or 0

        self.ratingAuthor = pRat * 3 + cRat
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.CASCADE, default=1)
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField('Category', related_name='post_categories', through='PostCategory')
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  # Новое поле для изображения

    def save(self, *args, **kwargs):
        self.text = self.censor_vulgar_words(self.text)
        super().save(*args, **kwargs)

    def censor_vulgar_words(self, text):
        vulgar_words = ['пидор', 'сука', 'редиска']
        for word in vulgar_words:
            text = text.replace(word, '*' * len(word))
        return text

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'

class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.text = self.censor_vulgar_words(self.text)
        super().save(*args, **kwargs)

    def censor_vulgar_words(self, text):
        vulgar_words = ['пидор', 'сука', 'редиска']
        for word in vulgar_words:
            text = text.replace(word, '*' * len(word))
        return text

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
