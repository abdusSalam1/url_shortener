# Generated by Django 2.2.1 on 2019-05-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.CharField(blank=True, max_length=300, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'url',
            },
        ),
    ]