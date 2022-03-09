from django import template
from random import sample


register = template.Library()


@register.filter()
def get_sample(skills_set):
    return sample(skills_set, 5)
