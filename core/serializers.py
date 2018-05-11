from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Interest, Member


class InterestSerializer(serializers.ModelSerializer):
    """
    Interest class serializer.
    """

    class Meta:
        model = Interest
        fields = ('id', 'name')

    extra_kwargs = {'id': {'read_only': False}}


class MemberSerializer(serializers.ModelSerializer):
    """
    Member class serializer.
    """
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    password = serializers.CharField(source='user.password')
    interests = InterestSerializer(many=True)

    class Meta:
        model = Member
        fields = ('id', 'username', 'first_name', 'last_name', 'password',
                  'gender', 'age', 'interests')

    extra_kwargs = {'id': {'read_only': True},
                    'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data.get('user'))

        member_data = dict(user=user, gender=validated_data.get('gender'),
                           age=validated_data.get('age'))
        member = Member.objects.create(**member_data)

        interest_names = [interest.get('name') for interest in
                          validated_data.pop('interests')]
        interests = Interest.objects.filter(name__in=interest_names)

        for interest in interests:
            member.interests.add(interest)

        return member
