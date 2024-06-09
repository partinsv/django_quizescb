# Generated by Django 5.0.6 on 2024-06-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_useranswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='duration',
            field=models.IntegerField(default=2, help_text='Duration of the quiz in minutes'),
            preserve_default=False,
        ),
    ]
