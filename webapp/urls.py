
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name=""),
    path('register/',views.register, name="register"),
    path('login/',views.loginUser, name="login"),
    path('logout/',views.logoutUser, name='logout'),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('create-record/',views.createRecord, name="create-record"),
    path('update-record/<int:pk>/',views.updateRecord, name="update-record"),
    path('record/<int:pk>/',views.viewRecord, name="record"),
    path('delete-record/<int:pk>/',views.deleteRecord, name="delete-record"),
    
]