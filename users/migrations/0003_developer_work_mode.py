# Generated by Django 4.1.5 on 2023-03-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_developer_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='work_mode',
            field=models.CharField(default='Work From Home', max_length=20),
        ),
    ]
