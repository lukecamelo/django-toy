# Generated by Django 2.1.7 on 2019-03-10 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='placeholder', max_length=200),
            preserve_default=False,
        ),
    ]
