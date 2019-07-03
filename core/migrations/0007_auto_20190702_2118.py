# Generated by Django 2.2.2 on 2019-07-03 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190702_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyrecord',
            name='date_recorded',
            field=models.DateField(help_text='Enter the date for your daily habit'),
        ),
        migrations.AlterUniqueTogether(
            name='dailyrecord',
            unique_together={('habit', 'date_recorded')},
        ),
    ]
