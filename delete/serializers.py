from rest_framework import serializers
from .models import Subscriber


class subscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('username', 'domain')
        fields = '__all__'
