from rest_framework import serializers
from users.models import CustomUser, UserProfile
from django.contrib.auth import (
    get_user_model,
    authenticate
    )

class CustomUserSerializer(serializers.ModelSerializer):
    """ User serializers"""
    class Meta:
        model = get_user_model()
        fields = ['user_id', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only':True, 'min_length': 5}}


    def create(self, validated_data):
        """Create and return user."""
        return get_user_model().objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user




