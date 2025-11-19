from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('update/<int:pk>',views.update,name='update'),
    path('trash/',views.trash,name='trash'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('restore/<int:pk>',views.restore,name='restore'),
    path('delete_permanent/<int:pk>',views.delete_permanent,name='delete_permanent'),
    path('restore_all/',views.restore_all,name='restore_all'),
    path('clear_all/',views.clear_all,name='clear_all'),
]