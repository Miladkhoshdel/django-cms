import os
from uuid import uuid4
from datetime import date


def upload_to(instance, filename):
    """For using file upload in post and page models"""
    dump, ext = os.path.splitext(filename)
    new_file_name = "".join((uuid4().urn, ext))
    path = instance.__class__.__name__
    return os.path.join(path, date.today().strftime("%Y/%m/%d"), new_file_name)
