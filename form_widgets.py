from django import forms
from django.forms import Field
from django.utils.html import format_html


class DisablePopulatedText(forms.Textarea):
    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget as an HTML string."""
        if value is not None:
            # Just return the value, as normal read_only fields do
            # Add Hidden Input otherwise the old fields are still required
            HiddenInput = forms.HiddenInput()
            return format_html("{}\n" + HiddenInput.render(name, value), self.format_value(value))
        else:
            return super().render(name, value, attrs, renderer)


def render_dynamic_crispy_formset(formset: object, formset_title: str) -> str:
    """Renders a formset using custom formset template, to be compatiblew with JS
    """
    from django.template.loader import render_to_string
    return render_to_string('contrib/dynamic_crispy_formset.html', {'formset': formset, 'formset_title': formset_title})


class Select2Modal(Field):
    """ Classe para usar um modal de select dinamico.
    """
    template_name = 'contrib/forms/widgets/select2modal.html'

    modal_title = ''
    url = ''
