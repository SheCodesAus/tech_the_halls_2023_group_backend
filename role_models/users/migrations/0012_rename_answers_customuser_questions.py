# Generated by Django 4.0.2 on 2023-03-26 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_rename_questions_customuser_answers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='answers',
            new_name='questions',
        ),
    ]