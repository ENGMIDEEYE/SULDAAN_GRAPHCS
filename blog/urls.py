from django.urls import path
from .views import Homeview,policy_view,terms_view,Posts,visitors,Visitors_create,Visior_delete,management_create,Management_delete,Management_update,Post_create,Post_delete,Category_view_list,Post_update_view,Managements,Category_update,Category_delete,Category_create



app_name = 'blog'

urlpatterns = [
    path('',Homeview,name="home"),
    path('privacy/',policy_view,name="privacy"),
    path('terms/',terms_view,name="terms"),
    path('visitors/',visitors,name="visitors"),
    path('posts/',Posts,name="posts"),
    path('category/',Category_view_list,name="category"),
    path('admin_page/',Managements,name="admin_page"),
    path('category/<int:pk>/update/',Category_update, name='category-update'),
    path('category/<int:pk>/delete/',Category_delete, name='category-delete'),
    path('category/add/',Category_create, name='category-create'),
    path('posts/<int:pk>/update/',Post_update_view, name='posts-update'),
    path('posts/<int:pk>/delete/',Post_delete, name='posts-delete'),
    path('posts/add/',Post_create, name='posts-create'),
    path('admin_page/add/',management_create, name='managemnet-create'),
    path('admin_page/<int:pk>/update/',Management_update, name='managemnet-update'),
    path('admin_page/<int:pk>/delete/',Management_delete, name='managemnet-delete'),
    path('visitors/add/',Visitors_create, name='visitors-create'),
    path('visitors/<int:pk>/delete/',Visior_delete, name='visitors-delete'),
]