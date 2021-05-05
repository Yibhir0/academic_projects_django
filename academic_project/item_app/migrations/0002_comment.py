# Generated by Django 3.2 on 2021-05-03 10:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('item_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_comment', models.CharField(max_length=500)),
                ('comment_date', models.DateTimeField(default=datetime.datetime(2021, 5, 3, 10, 53, 54, 280433, tzinfo=utc))),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item_app.project')),
            ],
        ),
    ]
