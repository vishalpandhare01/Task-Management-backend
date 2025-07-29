from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TaskModel
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

@receiver(post_save, sender=TaskModel)
def send_notification(sender, instance, created, **kwargs):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notifications',  # group name
            {
                'type': 'send_notification',
                'message': json.dumps({
                    'title': instance.status,
                    'message': instance.name,
                }),
            }
        )
