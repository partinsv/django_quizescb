# Generated by Django 5.0.6 on 2024-06-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0014_alter_quizaccess_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='quizaccess',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='quizaccess',
            name='quizzes',
            field=models.ManyToManyField(to='quizzes.quiz'),
        ),
        migrations.RemoveField(
            model_name='quizaccess',
            name='quiz',
        ),
    ]