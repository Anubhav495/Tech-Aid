from django.urls import path
from . import views
from users import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="user-login"),
    # path('login/',user_view.userlogin,name="user-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="user-logout"),
    path('register/', user_view.register, name="user-register"),
    path('profile/', user_view.profile, name="user-profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

