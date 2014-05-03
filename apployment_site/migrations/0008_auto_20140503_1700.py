# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apployment_site', '0007_auto_20140415_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('rated', models.ForeignKey(to='apployment_site.User', to_field=u'id')),
                ('rater', models.ForeignKey(to='apployment_site.User', to_field=u'id')),
                ('text', models.TextField()),
                ('stars', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
