# Generated by Django 4.0.2 on 2023-03-26 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_customuser_questions_alter_user_answers_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_answers',
            old_name='user_answer',
            new_name='answer',
        ),
        migrations.AlterField(
            model_name='user_answers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]