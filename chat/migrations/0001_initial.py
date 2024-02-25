# Generated by Django 3.2 on 2024-02-18 18:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('title_description', models.TextField()),
                ('chat_history', models.JSONField(null=True)),
            ],
        ),
    ]