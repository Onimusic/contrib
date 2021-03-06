from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from pathlib import Path


def validate_document_format(file):
    extension = Path(file.file.name).suffix
    if not extension in ['.doc', '.pdf', '.zip']:
        raise ValidationError(
            _('Invalid file format. Valid formats are .doc, .pdf or .zip')
        )


def validate_image_format(file):
    extension = Path(file.file.name).suffix
    if not extension in ['.png', '.jpg', '.jpeg']:
        raise ValidationError(
            _('Invalid file format. Valid formats are .png, .jpg or .jpeg')
        )


def validate_audio_format(file):
    extension = Path(file.file.name).suffix
    if extension != '.wav':
        raise ValidationError(
            _('Invalid file format. Please upload a .wav file')
        )


def validate_file_max_size(file, max_size_kb: int):
    file_size = file.file.size
    limit_kb = max_size_kb
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)


def validate_image_max_500(image):
    return validate_file_max_size(image, 500)


def validate_file_max_1000(file):
    return validate_file_max_size(file, 1000)


def validate_file_max_5000(file):
    return validate_file_max_size(file, 5000)


def validate_file_max_10000(file):
    return validate_file_max_size(file, 10000)


def validate_file_max_15000(file):
    return validate_file_max_size(file, 15000)


def validate_file_max_20000(file):
    return validate_file_max_size(file, 20000)


def validate_file_max_50000(file):
    return validate_file_max_size(file, 50000)


def validate_file_max_200000(file):
    return validate_file_max_size(file, 200000)


def validate_file_max_300000(file):
    return validate_file_max_size(file, 300000)
