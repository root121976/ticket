# Generated by Django 2.2.2 on 2019-06-20 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_tripinorder_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripinorder',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Status'),
        ),
    ]
