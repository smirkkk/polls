# Generated by Django 2.2.4 on 2020-05-07 12:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.Question')),
            ],
        ),
    ]