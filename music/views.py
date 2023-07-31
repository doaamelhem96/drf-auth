from django.shortcuts import render
from .models import Music
from .serializers import MusicSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .permissions import OwnerOnly

class MusiclistView(ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes =[OwnerOnly]