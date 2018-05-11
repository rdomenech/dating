import json

from django.core.management.base import BaseCommand

from core.models import Member
from core.utils import redis_cli


class Command(BaseCommand):
    help = 'It generates the initial scoring data'

    def handle(self, *args, **options):
        self.stdout.write('Starting scoring process...')
        redis_client = redis_cli()
        members = Member.objects.all()

        for member in members:
            member_data = member.calculate_score()
            redis_client.set(member.pk, json.dumps(member_data))

        self.stdout.write('{} members exported'.format(members.count()))
