from django.urls import path
from .views import *
urlpatterns = [
    path('blog/add/', CreateBlogView.as_view(), name='blog_add'),
    path('blog/', ListBlogView.as_view(), name='blog_list'),
    path('blog/list/ajax', ListBlogViewJson.as_view(), name='blog_list_ajax'),
    path('blog/edit/<int:pk>', UpdateBlogView.as_view(), name='blog_edit'),
    path('blog/delete/<int:pk>', DeleteBlogView.as_view(), name='blog_delete'),
]


