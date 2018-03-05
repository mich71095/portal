# Generated by Django 2.0.2 on 2018-03-05 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('order_id', models.CharField(blank=True, max_length=16, null=True)),
                ('invoice_date', models.DateTimeField()),
                ('terms', models.CharField(choices=[('Due of Receipt', 'Due of Receipt'), ('Due End of Next Month', 'Due End of Next Month'), ('Due End of Month', 'Due End of Month')], default='Due of Receipt', max_length=16)),
                ('due_date', models.DateTimeField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('conditions', models.CharField(blank=True, max_length=28, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Sent', 'Sent'), ('Draft', 'Draft')], default='Sent', max_length=16)),
            ],
        ),
    ]