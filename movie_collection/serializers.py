from rest_framework import serializers
from .models import User, Collection, Movies


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'])

        return user


# Login Serializer
# Register Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

# Collection serializer
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ("uuid", "title", "description")

# Movie Serializer
class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ("title", "description", "genres", "uuid")

# Movie Collection Serializer
class MovieCollectionSerializer(serializers.ModelSerializer):
    movies = MoviesSerializer(many=True)

    # Get Meta Data of user
    class Meta:
        model = Collection
        fields = ("uuid", "title", "description", "movies",)

    # Create and validate user data
    def create(self, validated_data):
        movies_data = validated_data.pop('movies')
        collection = Collection.objects.create(**validated_data, user=self.context.get("user"))
        for data in movies_data:
            Movies.objects.create(
                uuid=data["uuid"],
                title=data["title"],
                description=data["description"],
                genres=data["genres"],
                collection=collection
            )
        return collection

    # Update data
    def update(self, instance, validated_data):
        movies_data = validated_data.pop('movies')
        collection = super().update(instance, validated_data)
        for data in movies_data:
            Movies.objects.update_or_create(
                uuid=data["uuid"],
                collection=collection,
                defaults={
                    "uuid": data["uuid"],
                    "title": data["title"],
                    "description": data["description"],
                    "genres": data["genres"]
                }
            )
            return collection