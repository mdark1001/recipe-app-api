# Generated by Django 3.2.9 on 2021-11-04 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_survey_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='slug',
            field=models.SlugField(default='--'),
            preserve_default=False,
        ),
    ]
