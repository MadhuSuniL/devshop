# Generated by Django 4.1.5 on 2023-03-15 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='developer',
            options={'verbose_name_plural': 'Developers'},
        ),
        migrations.RenameField(
            model_name='developer',
            old_name='p_campany',
            new_name='p_company',
        ),
    ]