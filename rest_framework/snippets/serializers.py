from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet, Entitie, Site


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('site_name', 'site_year', 'site_title', 'type_chinese', 'type_english', 'home_title',
                  'my_mail', 'site_keywords', 'site_desc', 'domain_url', 'site_avatar', 'about_name', 'about_desc')


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code',
                  'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')


class EntitieSerializer(serializers.HyperlinkedModelSerializer):
    # entities = serializers.HyperlinkedRelatedField(many=True, view_name='entities', read_only=True)

    class Meta:
        model = Entitie
        fields = ('id', 'header', 'original_header', 'description', 'original_description', 'video', 'image',
                  'duration_raw', 'duration')
