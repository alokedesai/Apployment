# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apployment_site', '0002_auto_20140414_0543'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ratings',
            new_name='Rating',
        ),
    ]
