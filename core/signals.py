import json

from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Member
from core.utils import redis_cli

@receiver(post_save, sender=Member)
def my_handler(sender, instance, **kwargs):
    import pdb; pdb.set_trace()
    redis_client = redis_cli()
    member_data = instance.calculate_score()
    redis_client.set(instance.pk, json.dumps(member_data))
