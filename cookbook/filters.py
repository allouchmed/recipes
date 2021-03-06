import django_filters
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q
from cookbook.forms import MultiSelectWidget
from cookbook.models import Recipe, Keyword, Ingredient
from django.conf import settings
from django.utils.translation import gettext as _


class RecipeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method='filter_name')
    keywords = django_filters.ModelMultipleChoiceFilter(queryset=Keyword.objects.all(), widget=MultiSelectWidget,
                                                        method='filter_keywords')
    ingredients = django_filters.ModelMultipleChoiceFilter(queryset=Ingredient.objects.all(), widget=MultiSelectWidget,
                                                           method='filter_ingredients', label=_('Ingredients'))

    @staticmethod
    def filter_keywords(queryset, name, value):
        if not name == 'keywords':
            return queryset
        for x in value:
            queryset = queryset.filter(keywords=x)
        return queryset

    @staticmethod
    def filter_ingredients(queryset, name, value):
        if not name == 'ingredients':
            return queryset
        for x in value:
            queryset = queryset.filter(recipeingredient__ingredient=x).distinct()
        return queryset

    @staticmethod
    def filter_name(queryset, name, value):
        if not name == 'name':
            return queryset
        if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql_psycopg2':
            queryset = queryset.annotate(similarity=TrigramSimilarity('name', value), ).filter(
                Q(similarity__gt=0.1) | Q(name__icontains=value)).order_by('-similarity')
        else:
            queryset = queryset.filter(name__icontains=value)
        return queryset

    class Meta:
        model = Recipe
        fields = ['name', 'keywords', 'ingredients', 'internal']
