from django.urls import path
from . import views 

urlpatterns = [
    
    path('databukutabungan/', views.index, name='databukutabungan'),
    path('createbukutabungan/', views.createbukutabungan, name='createbukutabungan'),
    path('updatebukutabungan/<str:pk>', views.updatebukutabungan, name='updatebukutabungan'),
    path('deletebukutabungan/<str:pk>', views.deletebukutabungan, name='deletebukutabungan'),
    
]