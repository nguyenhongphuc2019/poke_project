from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from v1.models import Pokemon
from v1.serializers import PokemonSerializer


class PokemonViewSet(viewsets.ReadOnlyModelViewSet, APIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        return super().list(args)

    @action(detail=True, methods=['get'])
    def get_name_pokemon(self, request, pk=None):
        try:
            pokemon = Pokemon.objects.get(id=pk)
        except Pokemon.DoesNotExist:
            pokemon = None
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)
