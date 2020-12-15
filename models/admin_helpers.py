from django.urls import reverse


class GetAdminUrl():
    """
    Retorna a url do admin do objeto
    """
    def get_admin_url(self):
        return self.get_admin_url_by_id(self.id, self._meta.app_label, self._meta.model_name)

    @staticmethod
    def get_admin_url_by_id(element_id, app_label, model_name, site_url: str):
        return "{}{}".format(
            site_url,
            reverse(
                'admin:{}_{}_change'.format(
                    app_label,
                    model_name),
                args=(
                    element_id,))
        )
