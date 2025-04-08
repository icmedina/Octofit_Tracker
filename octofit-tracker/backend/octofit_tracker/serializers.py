from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'password']

class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    members = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = ['_id', 'name', 'members']

class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    user = ObjectIdField()

    class Meta:
        model = Activity
        fields = ['_id', 'user', 'activity_type', 'duration']

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    user = UserSerializer()

    class Meta:
        model = Leaderboard
        fields = ['_id', 'user', 'score']

class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()

    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description']