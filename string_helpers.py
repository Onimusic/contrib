from django.utils.html import format_html


def return_mark_safe(string):
    return format_html(string.replace("{", "{{").replace("}", "}}"))
