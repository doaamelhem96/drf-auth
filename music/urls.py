from django.urls import path
from .views import MusiclistView,MusicDetailView

urlpatterns = [
   
    
    path('', MusiclistView.as_view(),name="music_list"),
    path('<int:pk>/', MusicDetailView.as_view(),name="music_detail"),
    
]