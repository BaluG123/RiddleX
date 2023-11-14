# views.py

from rest_framework import generics
from .models import Level
from .serializers import LevelSerializer
from django.shortcuts import get_object_or_404

class LevelListView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LevelDetailView(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    lookup_field = 'level_number'  # Specify the field to use for the lookup

    def get_object(self):
        queryset = self.get_queryset()
        # Use the specified lookup field to filter the queryset
        filter_kwargs = {self.lookup_field: self.kwargs['level_number']}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj