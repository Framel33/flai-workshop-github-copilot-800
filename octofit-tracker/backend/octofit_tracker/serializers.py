from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'name', 'email', 'password', 'team', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True},
            '_id': {'read_only': True},
            'created_at': {'read_only': True}
        }


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at', 'members']
        extra_kwargs = {
            '_id': {'read_only': True},
            'created_at': {'read_only': True}
        }


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user_email', 'activity_type', 'duration', 'distance', 'calories', 'date', 'created_at']
        extra_kwargs = {
            '_id': {'read_only': True},
            'created_at': {'read_only': True}
        }


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user_email', 'user_name', 'team', 'total_calories', 'total_activities', 'total_duration', 'rank', 'updated_at']
        extra_kwargs = {
            '_id': {'read_only': True},
            'updated_at': {'read_only': True}
        }


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'activity_type', 'duration', 'difficulty', 'calories_estimate', 'created_at']
        extra_kwargs = {
            '_id': {'read_only': True},
            'created_at': {'read_only': True}
        }
