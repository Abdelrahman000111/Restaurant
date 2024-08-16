# Generated by Django 4.2.13 on 2024-05-26 13:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_alter_account_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('no_of_people', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
            options={
                'verbose_name': 'BookTable',
                'verbose_name_plural': 'BookTables',
            },
        ),
    ]
