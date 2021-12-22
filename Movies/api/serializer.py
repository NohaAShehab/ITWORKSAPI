from rest_framework import serializers
from Movies.models import Movie, WatchList


# for each model you need to define a serilizer

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     # calling ,,, POST
#     def create(self, validated_data):
#         print(validated_data)
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name")
#         instance.description = validated_data.get("description")
#         instance.active = validated_data.get("active")
#         instance.save()
#         return instance

class MovieSerializer(serializers.ModelSerializer):
    # modification
    len_name = serializers.SerializerMethodField()
    concat_desc = serializers.SerializerMethodField()

    class Meta:
        # perform all crud operations
        model = Movie
        fields = '__all__'
        # exclude = ("active",)

    def get_len_name(self, object):
        return len(object.name)

    def get_concat_desc(self, object):
        return f"{object.name}_{object.description}"


class WatchListSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        # perform all crud operations
        model = WatchList
        fields = '__all__'
        # exclude = ("active",)
