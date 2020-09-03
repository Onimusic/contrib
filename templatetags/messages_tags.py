from django import template

register = template.Library()


@register.simple_tag()
def get_bootstrap_alert_color(level_tag):
    if level_tag == 'success':
        return 'success'
    elif level_tag == 'debug':
        return 'dark'
    elif level_tag == 'info':
        return 'info'
    elif level_tag == 'warning':
        return 'warning'
    elif level_tag == 'error':
        return 'danger'
    else:
        return None
