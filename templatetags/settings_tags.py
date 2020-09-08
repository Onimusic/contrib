from django import template
from music_system.settings import local as settings

register = template.Library()


@register.simple_tag()
def get_settings_site_title(page_name):
    sitename = settings.FRONT_END__SITE_NAME
    if page_name and page_name != "":
        return "%s - %s" % (sitename, page_name)
    return sitename


@register.simple_tag()
def get_settings_site_url():
    return settings.SITE_URL
