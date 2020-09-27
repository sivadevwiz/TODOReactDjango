# Generated by Django 3.1.1 on 2020-09-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('userId', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('todoId', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]