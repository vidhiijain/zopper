import os
import uuid
from django.conf import settings
from django.db.models import FileField

from django.forms import forms
import os
import uuid
from django.utils.translation import ugettext_lazy as _


class MyFileField(FileField):

    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types")
        self.max_length = 300
        # self.max_upload_size = kwargs.pop("max_upload_size")

        super(MyFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(MyFileField, self).clean(*args, **kwargs)
        file = data.file
        try:
            content_type = file.content_type
            if content_type in self.content_types:
                pass
            else:
                raise forms.ValidationError(_('File type not supported.'))
        except AttributeError:
            pass
        return data

    def __init__(self, content_types=None, **kwargs):
        self.content_types = content_types
        # self.max_upload_size = max_upload_size
        super(MyFileField, self).__init__(**kwargs)


def _upload_and_rename(filename, media_dir):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(media_dir, filename)


def _upload_and_rename_csv(filename, media_dir):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(media_dir, filename)


def get_content_info_path(instance, filename):
    content_type = instance.content_type.encode('utf-8')
    content_type_name = content_type.lower()
    return _upload_and_rename_csv(filename, content_type_name)


# noinspection PyUnusedLocal
def upload_and_rename_csv(instance, filename):
    return _upload_and_rename_csv(filename, settings.CSV_FILE_PATH)