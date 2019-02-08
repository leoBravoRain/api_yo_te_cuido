from rest_framework import serializers
from .models import Dangers, Comment_To_Danger


# Serializer of dangers
class DangersSerializers(serializers.ModelSerializer):

    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Dangers
        # fields = ('id', 'latitude', 'longitude', 'comment','state','photo','date')
        fields = '__all__'

class Comment_To_Danger_Serializer(serializers.ModelSerializer):

	class Meta:

		model = Comment_To_Danger
		fields = '__all__'