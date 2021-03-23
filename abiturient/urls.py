from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.categories, name="categories"),
    path('tests/<int:category_id>/', views.tests, name="tests"),
    path('question/<int:test_id>/', views.questions, name="questions")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)