from django import template
from notifications.models import Notification

register = template.Library()


@register.simple_tag(name='unread_notifications_list')
def unread_notifications_list(user):
    return Notification.objects.filter(recipient_id=user.id).unread()
