from rest_framework import serializers
from aplications.users.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'user',
            'description',
            'cellphone',
            'phone',
            'profileImage',
        )