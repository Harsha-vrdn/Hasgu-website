# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.login_user, name="user_login"),
#     path("logout", views.logout_user, name="user_logout"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="user_login"),
    path("logout/", views.logout_user, name="user_logout"),
    path("register/", views.register_user, name="register_user"),
]
