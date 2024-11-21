from django.urls import path
from . import views




urlpatterns =[
    path('', views.staffs_list, name = 'Home'),
    path('create-profile/', views.create_profile, name = 'create'),
    path('edit-profile/<int:pk>/', views.update_profile, name = 'edit'),
    path('delete-profile/<int:pk>', views.delete_profile, name='delete'),
    path('staff/<int:pk>', views.Staffprofile, name = 'staff_profile' )
]

