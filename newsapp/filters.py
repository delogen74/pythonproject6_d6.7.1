from django import template
import re

register = template.Library()

CENSOR_WORDS = ['недопустимоеСлово1', 'недопустимоеСлово2']


@register.filter(name='censor')
def censor(text):
    if not isinstance(text, str):
        raise ValueError("The censor filter can only be applied to strings.")

    for word in CENSOR_WORDS:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub(lambda match: match.group()[0] + '*' * (len(match.group()) - 1), text)
    return text
