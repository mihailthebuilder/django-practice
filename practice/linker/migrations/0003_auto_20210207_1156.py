# Generated by Django 3.1.6 on 2021-02-07 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linker', '0002_message_votes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message_text',
            new_name='text_content',
        ),
        migrations.AlterField(
            model_name='message',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('votes', models.PositiveSmallIntegerField(default=0)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linker.message')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
