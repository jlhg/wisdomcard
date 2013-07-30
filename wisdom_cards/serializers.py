from django.contrib.auth.models import User
from wisdom_cards.models import WisdomCard
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class WisdomCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WisdomCard
        fields = ('section', 'contents')
