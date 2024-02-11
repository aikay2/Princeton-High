# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.validators import MaxLengthValidator


class Activity(models.Model):
    activityid = models.ForeignKey('Extracurricular', models.DO_NOTHING, db_column='activityID', blank=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentID', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'activity'


class Boarding(models.Model):
    student_id = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentID', blank=True)  # Field name made lowercase.
    bedspace = models.CharField(max_length=15, blank=True, null=True)
    allocated_hall = models.CharField(db_column='allocatedHall', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'boarding'


class Day(models.Model):
    student_id = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentID', blank=True)  # Field name made lowercase.
    transportation_mode = models.CharField(db_column='transportationMode', max_length=20, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'day'


class Extracurricular(models.Model):
    activity_id = models.AutoField(db_column='activityID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'extracurricular'


class Guardian(models.Model):
    guardian_id = models.CharField(db_column='guardianID', primary_key=True, max_length=10)  # Field name made lowercase.
    student_id = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentID', blank=False)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=False)
    home_address = models.CharField(db_column='homeAddress', max_length=120, blank=True)  # Field name made lowercase.
    occupation = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=11, db_column='phoneNumber', blank=False, validators=[MaxLengthValidator(limit_value=11)])  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guardian'
    
    def __str__(self):
        return self.name


class Lecture(models.Model):
    staff_id = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staffID', blank=True)  # Field name made lowercase.
    student_id = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentID', blank=True)  # Field name made lowercase.
    lecture_date = models.DateField(db_column='lectureDate', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lecture'


class Literary(models.Model):
    activity_id = models.ForeignKey(Extracurricular, models.DO_NOTHING, db_column='activityID', blank=True)  # Field name made lowercase.
    activities_participated = models.IntegerField(db_column='activitiesParticipated', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'literary'


class Prefect(models.Model):
    prefect_id = models.CharField(db_column='prefectID', primary_key=True, max_length=10)  # Field name made lowercase.
    student_id = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentID', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prefect'


class Principal(models.Model):
    staff_id = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staffID', blank=True)  # Field name made lowercase.
    qualification = models.CharField(max_length=30, blank=True)
    date_appointed = models.DateField(db_column='dateAppointed', blank=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'principal'


class Sport(models.Model):
    activity_id = models.ForeignKey(Extracurricular, models.DO_NOTHING, db_column='activityID', blank=True)  # Field name made lowercase.
    sport_name = models.CharField(db_column='sportName', max_length=20, blank=True)  # Field name made lowercase.
    games_played = models.IntegerField(db_column='gamesPlayed', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sport'


class Staff(models.Model):
    categories = [
        ('T', 'Teacher'),
        ('P', 'Principal'),
    ]

    staff_id = models.CharField(db_column='staffID', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    staff_type = models.CharField(db_column='staffType', max_length=1, blank=True, choices=categories)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staff'
    
    def __str__(self):
        return self.name.title()


class Student(models.Model):
    states = [
        'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno',
        'Cross River', 'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa',
        'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger',
        'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'
    ]

    enrollment_types = [
        ('D', 'Day'),
        ('B', 'Boarding'),
    ]

    prefectship = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    student_id = models.CharField(db_column='studentID', primary_key=True, max_length=7)
    name = models.CharField(max_length=70, blank=True, null=True)
    DOB = models.DateField(blank=True, null=True)
    enrollment_type = models.CharField(db_column='enrollmentType', max_length=1, blank=True, choices=enrollment_types)
    prefect_status = models.CharField(db_column='prefectStatus', max_length=1, blank=True, choices=prefectship)
    state_of_Origin = models.CharField(db_column='stateOfOrigin', max_length=25, blank=True, choices=[(state, state) for state in states])
    teacher = models.ForeignKey(Staff, models.DO_NOTHING, db_column='staffID', blank=True)

    def __str__(self):
        return self.name.title()

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    staff_id = models.ForeignKey(Staff, models.DO_NOTHING, db_column='staffID', blank=True)  # Field name made lowercase.
    field_of_study = models.CharField(db_column='fieldOfStudy', max_length=30, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teacher'

