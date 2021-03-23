from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('auth_teach/', views.auth_tech, name="auth_teach"),
    path('auth_abit/', views.register, name="auth_abit" ),
    # path('categories/',  views.categories, name="categories")
    path('categories/', include('abiturient.urls'), name = "abiturient"),
    #path('accounts/', include('django.contrib.auth.urls'), name = "accounts"),
    path('start_test/', views.start_test, name="star_test"),
    path('login/', views.LoginView, name='login')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)