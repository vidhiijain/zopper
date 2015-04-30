from django.db import models
import csv
from .helpers import MyFileField, upload_and_rename_csv
from django.core.files.storage import FileSystemStorage
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from south.modelsinspector import add_introspection_rules


csv_storage = FileSystemStorage(location=settings.CSV_FILE_PATH)
add_introspection_rules([], ["^indian_gov_app\.helpers\.MyFileField"])

class DataStore(models.Model):
    device_name = models.SlugField(max_length=255, unique=True)
    magnification = models.CharField(max_length=15, blank=True, null=True)
    field_of_view = models.CharField(max_length=15, blank=True, null=True)
    range = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.device_name


class CsvData(models.Model):
    name = models.CharField(max_length=64)
    file = MyFileField(upload_to=upload_and_rename_csv, storage=csv_storage, content_types=['text/csv'], max_length=1000)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(CsvData, self).save()


@receiver(post_save, sender=CsvData)
def signal_handler(sender, **kwargs):
    csv_name = kwargs.get('instance')

    file_path = str(csv_name.file)
    file_ptr = open(file_path)
    data_reader = csv.reader(file_ptr, delimiter=',')
    try:
        for row in data_reader:
            print "row -->", row
            ds = DataStore(device_name=row[0], magnification=row[1].strip(),
                           field_of_view=row[2].strip(), range=row[3].strip())
            ds.save()
    except Exception, e:
        print e
    print 'Data Processing Done'