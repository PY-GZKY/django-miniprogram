from rest_framework import serializers

from story.models import Slides, VehicleDetail, Vehicles, Stories


class SlidesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Slides
        fields = ('id', 'header', 'sub_header', 'description', 'image', 'created')

    def get_image(self, obj):
        image_url = obj.image.url
        return "https://127.0.0.1:8000/media/" + image_url


class VehicleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetail
        fields = ('id', 'header', 'description', 'image', 'created')


class VehiclesSerializer(serializers.ModelSerializer):
    vehicles = VehicleDetailSerializer(many=True)

    class Meta:
        model = Vehicles
        fields = ('id', 'header', 'description', 'image', 'vehicles', 'created')
        read_only_fields = ('id', 'header', 'description', 'image', 'vehicles', 'created')

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = (
            'id', 'header', 'original_header', 'description', 'original_description', 'video', 'image',
            'duration', 'created', 'updated')
        read_only_fields = (
            'id', 'header', 'original_header', 'description', 'original_description', 'video', 'image',
            'duration', 'created', 'updated')

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
