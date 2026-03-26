from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete-transaction/<id>/', views.delete_transaction, name="delete_transaction")
]