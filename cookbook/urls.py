from django.urls import path

from .views import *
from cookbook.views import api
from cookbook.helper import dal

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='view_books'),
    path('plan/', views.meal_plan, name='view_plan'),
    path('shopping/', views.shopping_list, name='view_shopping'),
    path('settings/', views.settings, name='view_settings'),

    path('view/recipe/<int:pk>', views.recipe_view, name='view_recipe'),

    path('new/recipe/', new.RecipeCreate.as_view(), name='new_recipe'),
    path('new/recipe_import/<int:import_id>/', new.create_new_external_recipe, name='new_recipe_import'),
    path('new/keyword/', new.KeywordCreate.as_view(), name='new_keyword'),
    path('new/storage/', new.StorageCreate.as_view(), name='new_storage'),
    path('new/book/', new.RecipeBookCreate.as_view(), name='new_book'),
    path('new/plan/', new.MealPlanCreate.as_view(), name='new_plan'),

    path('list/keyword', lists.keyword, name='list_keyword'),
    path('list/import_log', lists.sync_log, name='list_import_log'),
    path('list/import', lists.recipe_import, name='list_import'),
    path('list/storage', lists.storage, name='list_storage'),

    path('edit/recipe/<int:pk>/', edit.switch_recipe, name='edit_recipe'),
    path('edit/recipe/internal/<int:pk>/', edit.internal_recipe_update, name='edit_internal_recipe'),
    # for internal use only
    path('edit/recipe/external/<int:pk>/', edit.RecipeUpdate.as_view(), name='edit_external_recipe'),
    # for internal use only
    path('edit/recipe/convert/<int:pk>/', edit.convert_recipe, name='edit_convert_recipe'),  # for internal use only

    path('edit/keyword/<int:pk>/', edit.KeywordUpdate.as_view(), name='edit_keyword'),
    path('edit/sync/<int:pk>/', edit.SyncUpdate.as_view(), name='edit_sync'),
    path('edit/import/<int:pk>/', edit.ImportUpdate.as_view(), name='edit_import'),
    path('edit/storage/<int:pk>/', edit.edit_storage, name='edit_storage'),
    path('edit/comment/<int:pk>/', edit.CommentUpdate.as_view(), name='edit_comment'),
    path('edit/recipe-book/<int:pk>/', edit.RecipeBookUpdate.as_view(), name='edit_recipe_book'),
    path('edit/plan/<int:pk>/', edit.MealPlanUpdate.as_view(), name='edit_plan'),
    path('edit/ingredient/', edit.edit_ingredients, name='edit_ingredient'),

    path('redirect/delete/<slug:name>/<int:pk>/', delete.delete_redirect, name='redirect_delete'),

    path('delete/recipe/<int:pk>/', delete.RecipeDelete.as_view(), name='delete_recipe'),
    path('delete/recipe-source/<int:pk>/', delete.RecipeSourceDelete.as_view(), name='delete_recipe_source'),
    path('delete/keyword/<int:pk>/', delete.KeywordDelete.as_view(), name='delete_keyword'),
    path('delete/sync/<int:pk>/', delete.MonitorDelete.as_view(), name='delete_sync'),
    path('delete/import/<int:pk>/', delete.ImportDelete.as_view(), name='delete_import'),
    path('delete/storage/<int:pk>/', delete.StorageDelete.as_view(), name='delete_storage'),
    path('delete/comment/<int:pk>/', delete.CommentDelete.as_view(), name='delete_comment'),
    path('delete/recipe-book/<int:pk>/', delete.RecipeBookDelete.as_view(), name='delete_recipe_book'),
    path('delete/recipe-book-entry/<int:pk>/', delete.RecipeBookEntryDelete.as_view(), name='delete_recipe_book_entry'),
    path('delete/plan/<int:pk>/', delete.MealPlanDelete.as_view(), name='delete_plan'),

    path('data/sync', data.sync, name='data_sync'),  # TODO move to generic "new" view
    path('data/batch/edit', data.batch_edit, name='data_batch_edit'),
    path('data/batch/import', data.batch_import, name='data_batch_import'),
    path('data/sync/wait', data.sync_wait, name='data_sync_wait'),
    path('data/statistics', data.statistics, name='data_stats'),

    path('api/get_external_file_link/<int:recipe_id>/', api.get_external_file_link, name='api_get_external_file_link'),
    path('api/get_recipe_file/<int:recipe_id>/', api.get_recipe_file, name='api_get_recipe_file'),

    path('api/sync_all/', api.sync_all, name='api_sync'),

    path('dal/keyword/', dal.KeywordAutocomplete.as_view(), name='dal_keyword'),
    path('dal/ingredient/', dal.IngredientsAutocomplete.as_view(), name='dal_ingredient'),
    path('dal/unit/', dal.UnitAutocomplete.as_view(), name='dal_unit'),
]
