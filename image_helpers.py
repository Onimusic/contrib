import os

from io import BytesIO
from django.core.files import File
from PIL import Image


def make_thumbnail(image, size=(100, 100), filename=''):
    """Makes thumbnails of given size from given image"""
    if image:
        pil_image = Image.open(image).convert('RGB')
        pil_image.thumbnail(size)  # resize image
        # pil_image.convert('RGB') # convert mode
        thumb_io = BytesIO()  # create a BytesIO object
        pil_image.save(thumb_io, 'JPEG', quality=85)  # save image to BytesIO object
        thumbnail = File(thumb_io, name=filename)  # create a django friendly File object

        return thumbnail
    return None


def make_thumbnail_and_set_for_model(obj, image_fied, thumb_field):
    image = getattr(obj, image_fied, None)
    if image:
        cover_filename = os.path.basename(getattr(image, 'name', ''))
        image_thumbnail = getattr(obj, thumb_field, None)
        if not image_thumbnail or cover_filename != os.path.basename(
                getattr(image_thumbnail, 'name', '')):
            setattr(obj, thumb_field, make_thumbnail(image, size=(100, 100), filename=cover_filename))
