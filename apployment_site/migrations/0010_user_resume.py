# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apployment_site', '0009_auto_20140506_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='resume',
            field=models.FileField(null=True, upload_to='', blank=True),
            preserve_default=True,
        ),
    ]
