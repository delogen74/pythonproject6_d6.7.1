from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    vulgar_words = ['пидор', 'сука', 'редиска']
    for word in vulgar_words:
        value = value.replace(word, '*' * len(word))
    return value
