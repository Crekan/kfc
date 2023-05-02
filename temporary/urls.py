from django.urls import path

from temporary.views import TemporaryCreateView, TemporaryRetrieveUpdateDeleteView, TemporaryView

urlpatterns = [
    path('temporary/create/', TemporaryCreateView.as_view(), name='temporary_create'),
    path('temporary/<int:pk>/', TemporaryRetrieveUpdateDeleteView.as_view(), name='temporary_retrieve_update_delete'),
    path('temporary/', TemporaryView.as_view(), name='temporary'),
]
