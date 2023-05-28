from django.urls import path
from app import views

urlpatterns = [
    path('get-filtered-user/', views.filter_user, name="filtered_user"),
    path('register/', views.register)
]

