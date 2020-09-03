import pandas
from django.utils.translation import gettext as _


def get_blank_generic_file_from_fields(bulk_fields):
    """ Cria e retorna um arquivo xlsx de acordo com uma lista de campos
    """
    fields = dict()
    for bulk_field in bulk_fields:
        fields[bulk_field[0]] = ["#{}".format(bulk_field[1])]
    df = pandas.DataFrame.from_dict(fields)
    # noinspection PyPep8Naming
    from io import BytesIO as IO
    excel_file = IO()
    # noinspection PyTypeChecker
    excel_writer = pandas.ExcelWriter(excel_file, engine='xlsxwriter')
    df.to_excel(excel_writer, 'data', index=False)
    excel_writer.save()
    excel_writer.close()
    excel_file.seek(0)

    return excel_file.read()


def get_errors_messages_html(errors) -> str:
    """ Retorna um código html com uma lista ordenada de erros ou n/a
    """
    if errors is not None and errors != "":
        errors = str(errors).split("|")
        from django.utils.html import format_html
        return format_html('<br><ol>{}</ol>'.format("".join(["<li>{}</li>".format(error) for error in errors])))
    else:
        return _("n/a")
