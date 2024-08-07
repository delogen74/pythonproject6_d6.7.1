import django_filters
from django.forms import DateTimeInput
from .models import Post, Category

class PostFilter(django_filters.FilterSet):
    postCategory = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label='Категория',
        to_field_name='id'
    )
    date_after = django_filters.DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
        label='Позже указанной даты'
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }
