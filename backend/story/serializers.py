from rest_framework import serializers

from django_mini import settings
from story.models import Slides, VehicleDetail, Vehicles, Stories


class SlidesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Slides
        fields = ('id', 'header', 'sub_header', 'description', 'image', 'created')

    def get_image(self, obj):
        image_url = obj.image.url
        return settings.WEB_ROOT + image_url


class VehicleDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = VehicleDetail
        fields = ('id', 'header', 'description', 'image', 'created')

    def get_image(self, obj):
        image_url = obj.image.url
        return settings.WEB_ROOT + image_url


class VehiclesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    vehicles = VehicleDetailSerializer(many=True)

    class Meta:
        model = Vehicles
        fields = ('id', 'header', 'description', 'image', 'vehicles', 'created')
        read_only_fields = ('id', 'header', 'description', 'image', 'vehicles', 'created')

    def get_image(self, obj):
        image_url = obj.image.url
        return settings.WEB_ROOT + image_url

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class StoriesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()
    class Meta:
        model = Stories
        fields = (
            'id', 'header', 'original_header', 'description', 'original_description', 'video', 'image',
            'duration', 'created', 'updated')
        read_only_fields = (
            'id', 'header', 'original_header', 'description', 'original_description', 'video', 'image',
            'duration', 'created', 'updated')

    def get_image(self, obj):
        image_url = obj.image.url
        return settings.WEB_ROOT + image_url

    def get_video(self, obj):
        video_url = obj.video.url
        return settings.WEB_ROOT + video_url

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
