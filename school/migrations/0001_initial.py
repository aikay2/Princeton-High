# Generated by Django 5.0.1 on 2024-01-28 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'activity',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Boarding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedspace', models.CharField(blank=True, max_length=15, null=True)),
                ('allocatedhall', models.CharField(blank=True, db_column='allocatedHall', max_length=15, null=True)),
            ],
            options={
                'db_table': 'boarding',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transportationmode', models.CharField(blank=True, db_column='transportationMode', max_length=20)),
            ],
            options={
                'db_table': 'day',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Extracurricular',
            fields=[
                ('activityid', models.AutoField(db_column='activityID', primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'db_table': 'extracurricular',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('guardianid', models.CharField(db_column='guardianID', max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('homeaddress', models.CharField(blank=True, db_column='homeAddress', max_length=120)),
                ('occupation', models.CharField(blank=True, max_length=30)),
                ('phonenumber', models.IntegerField(blank=True, db_column='phoneNumber')),
            ],
            options={
                'db_table': 'guardian',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturedate', models.DateField(blank=True, db_column='lectureDate')),
            ],
            options={
                'db_table': 'lecture',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Literary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activitiesparticipated', models.IntegerField(blank=True, db_column='activitiesParticipated')),
            ],
            options={
                'db_table': 'literary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prefect',
            fields=[
                ('prefectid', models.CharField(db_column='prefectID', max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'prefect',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(blank=True, max_length=30)),
                ('dateappointed', models.DateField(blank=True, db_column='dateAppointed')),
            ],
            options={
                'db_table': 'principal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sportname', models.CharField(blank=True, db_column='sportName', max_length=20)),
                ('gamesplayed', models.IntegerField(blank=True, db_column='gamesPlayed')),
            ],
            options={
                'db_table': 'sport',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staffid', models.CharField(db_column='staffID', max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('stafftype', models.CharField(blank=True, db_column='staffType', max_length=1)),
            ],
            options={
                'db_table': 'staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentid', models.CharField(db_column='studentID', max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('enrollmenttype', models.CharField(blank=True, db_column='enrollmentType', max_length=1)),
                ('prefectstatus', models.CharField(blank=True, db_column='prefectStatus', max_length=1)),
                ('stateoforigin', models.CharField(blank=True, db_column='stateOfOrigin', max_length=25)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldofstudy', models.CharField(blank=True, db_column='fieldOfStudy', max_length=30)),
            ],
            options={
                'db_table': 'teacher',
                'managed': False,
            },
        ),
    ]
