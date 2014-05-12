# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apployment_site', '0014_delete_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='resume',
            field=models.FileField(null=True, upload_to='resume', blank=True),
        ),
    ]
