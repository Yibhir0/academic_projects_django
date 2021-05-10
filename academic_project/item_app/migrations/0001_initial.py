# Generated by Django 3.2 on 2021-05-10 13:39

from django.db import migrations, models
import django.utils.timezone
import item_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, validators=[item_app.models.checkRating])),
                ('likes', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=40)),
                ('project_type', models.CharField(max_length=35)),
                ('keyword_list', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=60)),
                ('url', models.URLField(blank=True)),
                ('status', models.CharField(help_text='Ex: Started, In Progress or Completed', max_length=15)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('snapshot', models.ImageField(default='project_default_pic.png', upload_to='project_images')),
            ],
        ),
    ]
