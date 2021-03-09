from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('profile/<str:pk>', views.ContactProfile, name='profile'),
    path('add-contact/', views.addContact, name='add-contact'),
    path('edit-contact/<str:pk>', views.editContact, name='edit-contact'),
    path('delete/<str:pk>', views.deleteContact, name='delete')
]
