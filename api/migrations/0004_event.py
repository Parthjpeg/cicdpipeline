# Generated by Django 4.0.6 on 2023-04-10 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_role_delete_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('mode', models.CharField(choices=[('1', 'Online'), ('2', 'Offline')], default='1', max_length=20)),
                ('address', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField()),
                ('Modrator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Modrator', to=settings.AUTH_USER_MODEL, to_field='username')),
                ('Performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Performer', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]