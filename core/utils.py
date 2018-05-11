import redis

from django.conf import settings


def redis_cli():
    redis_config = settings.REDIS_CONFIG
    return redis.Redis(host=redis_config.get('host'), port=redis_config.get(
        'port'), password=redis_config.get('password'))
