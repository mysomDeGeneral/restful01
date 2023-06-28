from rest_framework import serializers
from .models import Toy


class ToySerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=150)
    description = serializers.CharField(required=False)
    release_date = serializers.DateTimeField(required=False)
    toy_category = serializers.CharField(required=False, max_length=200)
    was_included_in_home = serializers.BooleanField(required=False)


    def create(self, validated_data):
        return Toy.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.toy_category = validated_data.get('toy_category', instance.toy_category)
        instance.was_included_in_home = validated_data.get('was_included_in_home', instance.was_included_in_home)
        instance.save()
        return instance
    