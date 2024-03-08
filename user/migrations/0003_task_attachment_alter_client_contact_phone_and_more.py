# Generated by Django 5.0.2 on 2024-03-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_submittask_alter_project_attachment_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='attachment',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='contact_phone',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Completed', 'Completed'), ('Rejected', 'Rejected'), ('Cancelled', 'Cancelled'), ('Revision', 'Revision'), ('Resubmission', 'Resubmission'), ('Pending', 'Pending')], default='New', max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Approved', 'Approved'), ('Completed', 'Completed'), ('Rejected', 'Rejected'), ('Cancelled', 'Cancelled'), ('Revision', 'Revision'), ('Resubmission', 'Resubmission'), ('Pending', 'Pending')], default='New', max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='writer',
            name='phone_number',
            field=models.CharField(max_length=30),
        ),
    ]
