# Generated by Django 4.2.7 on 2024-08-16 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Case', '0006_alter_case_insurer_alter_contact_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='insurer',
            field=models.CharField(choices=[('EML', 'EML'), ('Allianz', 'Allianz'), ('Suncorp', 'Suncorp'), ('GIO', 'GIO'), ('QBE', 'QBE')], max_length=100),
        ),
    ]
