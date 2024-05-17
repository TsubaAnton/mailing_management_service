# Generated by Django 5.0.3 on 2024-05-13 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_message_created_at_alter_message_updated_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
        migrations.RemoveField(
            model_name='message',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='message',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='message',
            name='uuid',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='clients',
            field=models.ManyToManyField(to='service.client'),
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt', models.BooleanField(verbose_name='Статус попытки')),
                ('attempt_time', models.DateTimeField(verbose_name='Дата и время последней попытки')),
                ('response', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ответ почтового сервера')),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.newsletter')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
            },
        ),
    ]
