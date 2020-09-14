from rest_framework import serializers
from v1.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta():
        model = Pokemon
        fields = '__all__'

    def create(self, validated_data):
        return Pokemon.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
