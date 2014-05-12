# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apployment_site', '0013_auto_20140512_1815'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Experience',
        ),
    ]
