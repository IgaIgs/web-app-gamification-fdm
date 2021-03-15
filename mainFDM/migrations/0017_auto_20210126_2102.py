# Generated by Django 3.1.4 on 2021-01-26 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainFDM', '0016_auto_20201222_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelperProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='helper', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='HelperAccount',
        ),
        migrations.AlterField(
            model_name='gamequestion',
            name='answer',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='gamequestion',
            name='question',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(blank=True),
        ),
    ]