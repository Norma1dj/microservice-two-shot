# Generated by Django 4.0.3 on 2023-07-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0004_binvo'),
    ]

    operations = [
        migrations.AddField(
            model_name='binvo',
            name='import_href',
            field=models.CharField(max_length=100, null=True),
        ),
    ]