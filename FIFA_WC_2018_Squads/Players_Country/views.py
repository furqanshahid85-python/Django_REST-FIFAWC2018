from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Squad
from .serializers import SquadSerializer

# List All the Players Data
class ListAllPlayers(generics.ListAPIView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer

# Retrieve a player data against a pk
class RetrievePlayer(generics.RetrieveAPIView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer


# Add a new player
class AddNewPlayer(generics.CreateAPIView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer

# Update an existing player
class UpdatePlayer(generics.UpdateAPIView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer

# Delete a player
class DeletePlayer(generics.DestroyAPIView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer



# List all players using Country_Name
# class ListPlayerCountry(generics.ListAPIView):
#     serializer_class = SquadSerializer
#     def get_queryset(self):
#         print(self.request)
#         return Squad.objects.all()
