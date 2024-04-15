from django.urls import path, include
from . import views

urlpatterns =[

    path('', views.apiOverview, name='api-overview'),
    path('blog-list/', views.blog_list, name='blog-list'),
    path('blog-details/<str:pk>', views.blogDetails, name='blog-details'),
    path('blog-create/', views.blogCreate, name='blog-create'),
    path('blog-update/<str:pk>', views.blogUpdate, name='blog-update'),
    path('blog-delete/<str:pk>', views.blogDelete, name='blog-delete'),

]