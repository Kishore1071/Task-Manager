from django.urls import path
from .views import *

urlpatterns = [
    path('sample/', sample_view, name='sample_view'),
    path('users/', user_list, name='user_list'),
    path('create/user/', create_user, name='create_user'),
    path('update/user/<int:user_id>/', update_user, name='update_user'),
    path('delete/user/<int:user_id>/', delete_user, name='delete_user'),
    path('', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]