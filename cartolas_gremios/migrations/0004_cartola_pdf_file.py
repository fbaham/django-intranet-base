# Generated by Django 2.2.1 on 2019-06-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartolas_gremios', '0003_auto_20190613_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartola',
            name='pdf_file',
            field=models.FileField(default='none', upload_to='core/media/cartolas_gremios/', verbose_name='Archivo PDF de cartola'),
            preserve_default=False,
        ),
    ]
