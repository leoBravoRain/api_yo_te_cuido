# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import DangersSerializers, Comment_To_Danger_Serializer, Area_Of_Company_Serializer, Suggestions_From_User_Serializer
from .models import Dangers, Comment_To_Danger, Area_Of_Company, Suggestions_From_User

# Generic view for get/post Suggestions_From_User
class Suggestions_From_User_View(generics.ListCreateAPIView):

    queryset = Suggestions_From_User.objects.all()
    serializer_class = Suggestions_From_User_Serializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

# generic view for get/post Dangers objects
class Dangers_Create_View(generics.ListCreateAPIView):

    queryset = Dangers.objects.all()
    serializer_class = DangersSerializers

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

# Generic view for get/post Areas of company objects
class Area_Of_Company_Create_View(generics.ListCreateAPIView):

    queryset = Area_Of_Company.objects.all()
    serializer_class = Area_Of_Company_Serializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

# View for videos location
class Dangers_Update_View(generics.ListCreateAPIView):
	
    # queryset = Videos_Location.objects.all()
    serializer_class = DangersSerializers

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

    # Filtering query set
    def get_queryset(self):

        # get location_id
        danger_id = self.kwargs['danger_id']

        # Get new state
        new_danger_state = self.kwargs["new_danger_state"]

        # Filter by location id
        danger = Dangers.objects.filter(id__exact = danger_id)

        # Get danger form array
        danger0 = danger[0]

        # Fix. Add state state = not state. This is not working because query_set method call twice time. I dont know why.
        # danger0.state = False
        danger0.state = new_danger_state

        # Save danger
        danger0.save()

        # Return queryset
        return danger

# Manage comments of danger
class Danger_Details_View(generics.ListCreateAPIView):

    # queryset = Videos_Location.objects.all()
    serializer_class = Comment_To_Danger_Serializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

    # Filtering query set
    def get_queryset(self):

        # get location_id
        danger_id = self.kwargs['danger_id']

        # Filter by location id
        comments = Comment_To_Danger.objects.filter(danger__id__exact = danger_id)

        # Return queryset
        return comments