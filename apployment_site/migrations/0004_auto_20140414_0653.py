# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apployment_site', '0003_auto_20140414_0549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password_description',
            new_name='description',
        ),
    ]
