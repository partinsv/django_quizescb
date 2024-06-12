# Generated by Django 5.0.6 on 2024-06-12 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0008_useractivitylog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct_option',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option4',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='selected_option',
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('single', 'Single Choice'), ('multiple', 'Multiple Choice')], default='single', max_length=8),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.question')),
            ],
        ),
        migrations.AddField(
            model_name='useranswer',
            name='selected_options',
            field=models.ManyToManyField(to='quizzes.option'),
        ),
    ]
