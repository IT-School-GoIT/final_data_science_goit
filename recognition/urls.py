from django.urls import path
from . import views


app_name = "recognition"

urlpatterns = [
    path('', views.index, name='index2'),
    path('result/<int:image_id>/', views.result, name='result'),
]
