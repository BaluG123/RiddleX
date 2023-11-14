# urls.py

from django.urls import path
from .views import LevelListView, LevelDetailView

urlpatterns = [
    path('levels/', LevelListView.as_view(), name='level-list'),
    path('levels/<int:level_number>/', LevelDetailView.as_view(), name='level-detail'),
]
