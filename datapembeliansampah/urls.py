from django.urls import path
from . import views 

urlpatterns = [
    
    path('datapembeliansampah/', views.index, name='datapembeliansampah'),
    path('createpembeliansampah/', views.createpembeliansampah, name='createpembeliansampah'),
    path('updatepembeliansampah/<str:pk>', views.updatepembeliansampah, name='updatepembeliansampah'),
    path('deletepembeliansampah/<str:pk>', views.deletepembeliansampah, name='deletepembeliansampah'),
    
]