"""
для обработки ошибки  404 рекомендуется создать отдельный view в папке проекта
"""
from django.shortcuts import render

from articles.models import Category


# фунцкия для обработки ошибки 404 page not found
def page_not_found_view(request, exception):
    return render(request, '404_not_found.html', status=404,
                  context={'menu_links': Category.objects.all().order_by('name')})