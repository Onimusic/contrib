from django.urls import reverse

from music_system.settings import local as settings


class GetAdminUrl():
    def get_admin_url(self):
        return self.get_admin_url_by_id(self.id, self._meta.app_label, self._meta.model_name)

    @staticmethod
    def get_admin_url_by_id(id, app_label, model_name):
        return "{}{}".format(
            settings.SITE_URL,
            reverse(
                'admin:{}_{}_change'.format(
                    app_label,
                    model_name),
                args=(
                    id,))
        )
