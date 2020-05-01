# Generated by Django 3.0.5 on 2020-04-30 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userform', '0002_auto_20200426_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('roomtypeid', models.AutoField(db_column='RoomTypeID', primary_key=True, serialize=False)),
                ('roomtype', models.CharField(db_column='RoomType', max_length=20)),
            ],
            options={
                'db_table': 'RoomType',
                'managed': True,
            },
        ),
    ]