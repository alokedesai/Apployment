# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apployment_site', '0011_user_gpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stars',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='school_type',
            field=models.CharField(default='Liberal Arts College', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='school_location',
            field=models.CharField(default='Claremont, CA', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='wage',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='resume',
            field=models.FileField(null=True, upload_to='/', blank=True),
        ),
    ]
