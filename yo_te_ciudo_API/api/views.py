# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import DangersSerializers, Comment_To_Danger_Serializer
from .models import Dangers, Comment_To_Danger

# generic view for get/post Dangers objects
class Dangers_Create_View(generics.ListCreateAPIView):

    queryset = Dangers.objects.all()
    serializer_class = DangersSerializers

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

        print "query_set method"

        # get location_id
        danger_id = self.kwargs['danger_id']

        # Filter by location id
        danger = Dangers.objects.filter(id__exact = danger_id)

        danger0 = danger[0]

        # Fix. Add state state = not state. This is not working because query_set method call twice time. I dont know why.
        danger0.state = False

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