from django import template
from django.template.defaultfilters import stringfilter

from articles.models import Comment, ArticleLike, Category

register = template.Library()


@register.filter
def rm_obs_pages(data):
    if 'page' in data:
        data._mutable = True
        data.pop('page')
        data._mutable = False
    return data.urlencode()


@register.filter
@stringfilter
def get_comments_count(article_guid):
    return str(Comment.count(article_guid))


@register.filter
@stringfilter
def get_likes_count(article_guid):
    return str(ArticleLike.count(article_guid))


@register.simple_tag(name='author_name')
def get_user_name(article):
    if article.author_id.first_name or article.author_id.last_name:
        return ' '.join([article.author_id.first_name, article.author_id.last_name])
    return article.author_id.username


@register.simple_tag(name='artcats')
def get_article_categories(article_guid):
    return Category.objects.filter(articlecategory__article_guid=article_guid)