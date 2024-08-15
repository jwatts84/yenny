# Generated by Django 4.2.7 on 2024-08-02 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwoShotPrompt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('instructions', models.TextField()),
                ('input1', models.TextField()),
                ('output1', models.TextField()),
                ('input2', models.TextField()),
                ('output2', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Two-Shot Prompts',
            },
        ),
    ]
