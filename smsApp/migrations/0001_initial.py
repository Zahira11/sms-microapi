# Generated by Django 3.0.7 on 2020-06-29 16:36

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('phoneNumber', models.CharField(max_length=100, unique=True)),
                ('otp', models.CharField(max_length=6)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupID', models.UUIDField()),
                ('groupName', models.CharField(max_length=80)),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=80)),
                ('account_sid', models.CharField(blank=True, max_length=80, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, default='Sent', max_length=100, null=True)),
                ('messageStatus', models.CharField(choices=[('D', 'D'), ('S', 'S'), ('F', 'F'), ('R', 'R'), ('SC', 'SC')], default='D', max_length=2)),
                ('dateScheduled', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receipent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsApp.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/uploads'), upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('messageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsApp.Message')),
            ],
        ),
    ]
