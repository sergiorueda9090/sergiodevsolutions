from rest_framework import serializers
from .models import DetailPage

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailPage
        fields = ['id', 'title', 'slug', 'image', 'subTile', 'myDescription', 'imageDescription', 'titleBenefits']