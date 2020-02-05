from rest_framework import serializers
from .models import Kind, SubKind, CustomUser, Advert


class BaseCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
        ]


class CustomUserSerializer(BaseCustomUserSerializer):
    class Meta(BaseCustomUserSerializer.Meta):
        fields = BaseCustomUserSerializer.Meta.fields + [
            'first_name',
            'last_name',
            'phone',
            'city'
        ]


class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = [
            'id',
            'name'
        ]


class SubKindSerializer(serializers.ModelSerializer):
    kind = KindSerializer()

    class Meta:
        model = SubKind
        fields = [
            'id',
            'name',
            'kind'
        ]


class BaseAdvertSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'name',
            'short_description',
            'price',
            'primary_avatar'
        ]

    def get_short_description(self, obj):
        return obj.description[:140]


class AdvertSerializer(serializers.ModelSerializer):
    class Meta(BaseAdvertSerializer.Meta):
        fields = BaseAdvertSerializer.Meta.fields + [
            'user',
            'avatars',
            'kind',
            'description',
            'price',
            'added',


        ]

class ImageForAdvertSerializer(serializers.ModelSerializer):
    pass
    # составной id обьявления + картинок

