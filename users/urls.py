from django.urls import path

from .views import UserList, UserDetail

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
]
