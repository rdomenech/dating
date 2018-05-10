import random
from tqdm import tqdm

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Factory

from core.models import Interest, Member

class Command(BaseCommand):
    help = 'Generates fake users for testing purposes.'

    def add_arguments(self, parser):
        parser.add_argument('number_of_members', nargs=1, type=int)

    def handle(self, *args, **options):
        number_of_members = options.get('number_of_members')[0]

        self.stdout.write('Creating {} members'.format(number_of_members))

        faker = Factory.create()

        if Interest.objects.all().count() < 10:
            for _ in tqdm(range(10)):
                Interest.objects.create(name=faker.word())

        interests = Interest.objects.values_list('id', flat=True)

        for _ in tqdm(range(number_of_members)):
            name = faker.name()

            user = User.objects.create_user(
                username=faker.email(),
                first_name=name.split(' ')[0],
                last_name=name.split(' ')[1],
                password='test_password01')

            member = Member.objects.create(
                user=user,
                gender=random.choice([Member.FEMALE, Member.MALE]),
                age=random.randint(0, 100))

            for interest in random.sample(list(interests), 3):
                member.interests.add(interest)

        self.stdout.write('Process finished...')

