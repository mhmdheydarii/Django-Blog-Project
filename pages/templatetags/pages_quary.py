from django import template
from pages.models import *

register = template.Library()

@register.inclusion_tag("includes/latest-post.html")
def latest_post():
    latest_post_object = Post.objects.filter(status=True)[:3]
    return {"latest_post_object":latest_post_object}
