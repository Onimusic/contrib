from django import template

register = template.Library()


@register.simple_tag()
def get_settings_site_title(page_name, front_end_site_name: str):
    sitename = front_end_site_name
    if page_name and page_name != "":
        return "%s - %s" % (sitename, page_name)
    return sitename


@register.simple_tag()
def get_settings_site_url(site_url: str):
    return site_url
