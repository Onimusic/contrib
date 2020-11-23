from django.core.exceptions import ValidationError
from django.db import transaction
# from notifications.signals import notify
# from post_office import mail
from django.utils.translation import gettext as _


def send_mail(recipients: list, template: str, context: dict, subject: str):
    """Default function for sending emails
    Args:
        recipients
        template
        context
        subject
    """
    pass
    # mail.send(
    #     recipients,
    #     # subject=subject,
    #     template=template,
    #     context=context,
    # )


@transaction.atomic
def process_notification(author, recipients, verb, target, url,
                         send_email,
                         email_template,
                         email_subject,
                         email_title,
                         email_description,
                         email_button_text,
                         email_url,
                         email_logo,
                         email_master_client_name):
    """Default system notification sender
    Sends bell notifications and email notifications, if specified. The atomic transaction decorator
    makes sure that email notifications are sent along with the bell ones. After an email is sent, the
    'emailed' field on the notification model should be set to True.
    Args:
        author: obj
        recipients: QuerySet
        verb: str
        target: obj
        url: str
        send_email: bool
        email_template: str(EmailTemplate object name)
        email_title
        email_subject
        email_description
        email_button_text
        email_url
        email_logo
        email_master_client_name
    """

    # bell notification
    # notify.send(sender=author, recipient=recipients, verb=verb, target=target, url=url, emailed=send_email)
    # todo quando o ator da notificacao for um usuario, colocar o nome dele como ator pra melhorar a legibilidade

    # email notification management
    if send_email:
        context = email_context_builder(email_url, email_title, email_subject, email_description, email_button_text,
                                        email_logo, email_master_client_name)
        email_recipients = []
        for recipient in recipients:
            email_recipients.append(recipient.email)

            if recipient.email is not None and recipient.email != '':
                email_recipients.append(recipient.email)
        try:
            send_mail(recipients=email_recipients, subject=email_subject, template=email_template,
                      context=context)
        except ValidationError:
            pass
        # @todo log
        # setting the emailed field on the notification sent as true


def email_context_builder(email_url, email_title, email_subject, email_description, email_button_text, email_logo,
                          email_master_client_name, support_mail: str, front_end_site_name: str):
    context = dict()
    email_support = _('Any questions? Email us!')
    email_support_mail = support_mail
    email_site_name = front_end_site_name
    context['url'] = email_url
    context['email_title'] = email_title
    context['email_subject'] = email_subject
    context['email_description'] = email_description
    context['email_button_text'] = email_button_text
    context['email_support'] = email_support
    context['email_support_mail'] = email_support_mail
    context['email_site_name'] = email_site_name
    context['publisher_logo_path'] = email_site_name
    context['email_logo'] = email_logo
    context['email_master_client_name'] = email_master_client_name
    return context
