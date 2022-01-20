from rest_framework import serializers

from story.models import Slides, VehicleDetail, Vehicles


class SlidesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slides
        fields = ('header', 'sub_header', 'description', 'image', 'created')


class VehicleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetail
        fields = ('header', 'description', 'image', 'created')


class VehiclesSerializer(serializers.ModelSerializer):
    vehicles = VehicleDetailSerializer(many=True)

    class Meta:
        model = Vehicles
        fields = ('header', 'description', 'image', 'vehicles', 'created')
        read_only_fields = ('header', 'description', 'image', 'vehicles', 'created')

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
