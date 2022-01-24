from rest_framework import serializers

from django_mini import settings
from story.models import Slides, VehicleDetail, Vehicles, Stories, StorieDetail


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

class StorieDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    stories = serializers.SerializerMethodField()
    # description = serializers.SerializerMethodField()

    class Meta:
        model = StorieDetail
        fields = (
            'id', 'stories', 'header', 'image', 'created', 'updated')
        read_only_fields = (
            'id', 'stories', 'header', 'image', 'created', 'updated')

    def get_image(self, obj):
        image_url = obj.image.url
        return settings.WEB_ROOT + image_url

    def get_stories(self, obj):
        header = obj.stories.header
        return header

    # def get_description(self, obj):
    #     description = obj.stories.description
    #     return description

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

class StoriesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    stories = StorieDetailSerializer(many=True)

    class Meta:
        model = Stories
        fields = (
            'id', 'header', 'description', 'image', 'stories', 'created', 'updated')
        read_only_fields = (
            'id', 'header', 'description', 'image',  'stories', 'created', 'updated')

    def get_image(self, obj):
        image_url = obj.image.url
        return settings.WEB_ROOT + image_url

    # def get_storie_list(self, obj):
    #     storie_list = obj.storie_detail_set.all()
    #     return storie_list

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


