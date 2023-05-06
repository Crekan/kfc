from rest_framework import generics

from .models import Temporary
from .serializers import TemporaryCreateSerializer, TemporarySerializer


class TemporaryCreateView(generics.CreateAPIView):
    serializer_class = TemporaryCreateSerializer

    def get_queryset(self):
        return Temporary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TemporaryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TemporaryCreateSerializer

    def get_queryset(self):
        return Temporary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TemporaryView(generics.ListAPIView):
    serializer_class = TemporarySerializer

    def get_queryset(self):
        return Temporary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
