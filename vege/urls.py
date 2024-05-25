from django.urls import path
from . import views
from core import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_page),
    path('add-recipes/', views.recipe, name="add-recipe"),
    path('recipes/', views.import_recipe, name="recipe"),
    path('delete_recipe/<id>/', views.delete_recipe, name='delete_recipe'),
    path('update_recipe/<id>/', views.update_recipe, name='update_recipe'),
    path('login/', views.login_page, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_page, name="logout")
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
