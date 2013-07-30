import random
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.renderers import UnicodeJSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from wisdom_cards.serializers import UserSerializer, WisdomCardSerializer
from wisdom_cards.models import WisdomCard


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class WisdomCardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WisdomCard.objects.all()
    serializer_class = WisdomCardSerializer
    permission_classes = (AllowAny,)
    renderer_classes = (UnicodeJSONRenderer,)


class RandomWisdomCardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WisdomCard.objects.all()
    serializer_class = WisdomCardSerializer
    permission_classes = (AllowAny,)
    renderer_classes = (UnicodeJSONRenderer,)

    def list(self, request):
        count = WisdomCard.objects.all().count()
        if count > 0:
            query = WisdomCard.objects.get(pk=random.randint(1, count))
        else:
            query = WisdomCard.objects.filter(pk=0)

        serializer = WisdomCardSerializer(query)
        return Response(serializer.data)
