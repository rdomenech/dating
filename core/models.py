from operator import itemgetter

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Interest(models.Model):
    """
    It represents the member's interest.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Member(models.Model):
    """
    It represents the platform's member.
    """

    MALE = 0
    FEMALE = 1

    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, default=MALE, validators=[MinValueValidator(0)])
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)])
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    def calculate_score(self):
        """
        It calculates the scores for the given member.
        :return: list of dicts with all the scores.
        """
        from core.serializers import MemberSerializer

        members = Member.objects.all()

        scoring_list = []
        for member in members:
            if self.pk == member.pk:
                continue

            member_data = MemberSerializer(member).data
            member_data['scoring'] = 0

            if self.gender != member_data['gender']:
                member_data['scoring'] += 100

            member_data['scoring'] += 100 - abs(self.age - member_data['age'])

            member_interests = [interest.name for interest in
                                self.interests.all()]
            other_member_interests = [interest['name'] for interest in
                                      member_data['interests']]

            member_data['scoring'] += len(set(member_interests) &
                                         set(other_member_interests)) * 100

            scoring_list.append(member_data)

        return sorted(scoring_list, key=itemgetter('scoring'), reverse=True)
