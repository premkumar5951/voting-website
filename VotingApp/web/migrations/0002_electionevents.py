# Generated by Django 4.2 on 2023-04-11 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_started', models.BooleanField(default=False)),
                ('is_ongoing', models.BooleanField(default=False)),
                ('is_ended', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('logo', models.ImageField(default='images/events/d_logo.png', upload_to='images/events')),
                ('description', models.CharField(max_length=500, unique=True)),
                ('event_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('parties', models.ManyToManyField(to='web.electionparties')),
            ],
        ),
    ]