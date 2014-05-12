# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apployment_site', '0010_user_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gpa',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
