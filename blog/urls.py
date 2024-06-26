from django.urls import path
from blog.views import register_user, login_user, post_list, post_detail, add_comment, add_post_list, online_users, \
    share_post

urlpatterns = [
    path('api/register/', register_user, name='register_user'),
    path('api/login/', login_user, name='login_user'),
    path('share-post/<str:profile_id>', share_post),
    path('api/all-posts/<str:profile_id>', post_list),
    path('api/posts/', add_post_list, name='add_post_list'),
    path('api/posts/<int:pk>/', post_detail, name='post_detail'),
    path('api/posts/<int:pk>/comments/', add_comment, name='add_comment'),
    path('online_users/', online_users, name='online_users'),
]
