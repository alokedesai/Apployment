# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apployment_site', '0012_auto_20140512_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='hasexperience',
            name='company',
            field=models.CharField(default='Pomona College', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hasexperience',
            name='title',
            field=models.CharField(default='Teaching Assistance', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hasexperience',
            name='description',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='hasexperience',
            name='experience',
        ),
    ]
