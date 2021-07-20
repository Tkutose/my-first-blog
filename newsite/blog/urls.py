from django.urls import path
from . import views

# 複数app存在時に区別するための名前空間
app_name = 'blogs'


urlpatterns = [
    path('', views.post_list, name='post_list'),

    # pkという名前で渡す
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), 
]
