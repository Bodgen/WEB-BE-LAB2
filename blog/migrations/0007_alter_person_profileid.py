# Generated by Django 5.0.6 on 2024-06-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_person_profileid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profileId',
            field=models.CharField(default='05eda096-9218-4e81-b9b2-d41d2ba0b2bc', max_length=255),
        ),
    ]
