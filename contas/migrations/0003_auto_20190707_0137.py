# Generated by Django 2.2.3 on 2019-07-07 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_transacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
