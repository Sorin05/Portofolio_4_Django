# Generated by Django 3.2.14 on 2022-07-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220708_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Added')], default=0),
        ),
    ]
