from django.urls import path
from .views import Postview, PostDetail, CreatePost
from .views import EditPost, DeletePost, user_logout


urlpatterns = [
    path('post/<int:pk>/delete', DeletePost.as_view(),name = 'deletepost'),
    path('post/<int:pk>/edit', EditPost.as_view(), name = 'editpost'),
    path('post/new', CreatePost.as_view(), name = 'newpost'),
    path('post/<int:pk>', PostDetail.as_view(), name = 'detailpage'),
    path('', Postview.as_view(), name = 'homepage'),
    path('logout', user_logout, name='logout')
]