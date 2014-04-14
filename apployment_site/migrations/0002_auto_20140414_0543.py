# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apployment_site', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratings',
            old_name='start',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='hasexperience',
            old_name='Experience',
            new_name='experience',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=200),
        ),
    ]
