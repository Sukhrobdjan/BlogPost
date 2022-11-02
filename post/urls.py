from django.urls import path
from .import views


urlpatterns = [

 path('', views.post_list, name='post_list'),
 path('post/<slug:slug>', views.post_detail, name='post_det'),
 path('tag/<slug:tag_slug>', views.post_detail, name='post_tag'),
]