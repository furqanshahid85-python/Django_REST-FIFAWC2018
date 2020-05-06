from rest_framework import serializers
from .models import Squad


# serializer class for Model Squad
class SquadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squad
        fields = '__all__'
