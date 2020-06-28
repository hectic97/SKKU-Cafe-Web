# Generated by Django 2.2.7 on 2019-12-07 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_evaluation'),
        ('review', '0002_facilityreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='moodreview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_text', models.CharField(max_length=200)),
                ('m_votes', models.IntegerField(default=0)),
                ('m_build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.building')),
            ],
        ),
    ]