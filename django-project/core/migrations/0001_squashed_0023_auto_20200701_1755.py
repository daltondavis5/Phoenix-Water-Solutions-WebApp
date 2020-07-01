# Generated by Django 3.0.7 on 2020-07-01 18:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Utility',
            fields=[
                ('type', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UtilityProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_measurement', models.FloatField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='core.Location')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Provider')),
                ('utility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Utility')),
            ],
        ),
        migrations.AddField(
            model_name='provider',
            name='utilities',
            field=models.ManyToManyField(through='core.UtilityProvider', to='core.Utility'),
        ),
        migrations.AlterField(
            model_name='utilityprovider',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to='core.Provider'),
        ),
        migrations.AlterField(
            model_name='utilityprovider',
            name='utility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utility', to='core.Utility'),
        ),
        migrations.AlterField(
            model_name='utilityprovider',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location'),
        ),
        migrations.AlterField(
            model_name='utilityprovider',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Provider'),
        ),
        migrations.AlterField(
            model_name='utilityprovider',
            name='utility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Utility'),
        ),
        migrations.AlterField(
            model_name='utilityprovider',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utilityproviders', to='core.Location'),
        ),
        migrations.AlterField(
            model_name='utilityprovider',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utilityproviders', to='core.Provider'),
        ),
        migrations.AlterField(
            model_name='utilityprovider',
            name='utility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utilityproviders', to='core.Utility'),
        ),
        migrations.AlterField(
            model_name='utilityprovider',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location'),
        ),
        migrations.AlterField(
            model_name='utilityprovider',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Provider'),
        ),
        migrations.AlterField(
            model_name='utilityprovider',
            name='utility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Utility'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField()),
                ('attribute', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Property')),
                ('billing_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('installed_date', models.DateField(default=django.utils.timezone.now)),
                ('uninstalled_date', models.DateField(blank=True, null=True)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Unit')),
                ('utility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Utility')),
            ],
        ),
        migrations.CreateModel(
            name='NewAccountFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('priority', models.IntegerField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')])),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Property')),
            ],
        ),
        migrations.CreateModel(
            name='LateFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('days_late', models.IntegerField()),
                ('priority', models.IntegerField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')])),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Property')),
            ],
        ),
        migrations.CreateModel(
            name='AdminFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('priority', models.IntegerField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')])),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Property')),
            ],
        ),
        migrations.CreateModel(
            name='RecollectionFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('priority', models.IntegerField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')])),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Property')),
                ('usage_based_split', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MeterError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error_date', models.DateField()),
                ('description', models.TextField(max_length=200)),
                ('repair_date', models.DateField(blank=True, null=True)),
                ('meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Meter')),
            ],
        ),
        migrations.CreateModel(
            name='MeterRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_date', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Meter')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyUtilityProviderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowance_units', models.FloatField(default=0)),
                ('bill_period_day', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('bill_post_day', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('default_usage', models.FloatField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Property')),
                ('utility_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UtilityProvider')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='utility_provider',
            field=models.ManyToManyField(through='core.PropertyUtilityProviderInfo', to='core.UtilityProvider'),
        ),
    ]
