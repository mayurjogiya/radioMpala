# Generated by Django 4.2.10 on 2024-07-28 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Surapuradada', '0006_alter_logs_browser_alter_logs_logid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]