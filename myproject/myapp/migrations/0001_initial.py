# Generated by Django 5.1.2 on 2024-10-22 10:26

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=254, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('role', models.CharField(choices=[('student', 'Student'), ('trainer', 'Trainer'), ('admin', 'Admin')], max_length=10)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='user_profile_pics/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('alternate_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('landmark', models.CharField(blank=True, max_length=255, null=True)),
                ('locality', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('pincode', models.CharField(blank=True, max_length=25, null=True)),
                ('state', models.CharField(blank=True, default='Maharashtra', max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=25, null=True)),
                ('linkedin_id', models.CharField(blank=True, max_length=255, null=True)),
                ('github_id', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('class_mode', models.CharField(blank=True, choices=[('offline', 'Offline'), ('online', 'Online'), ('hybrid', 'Hybrid')], max_length=100, null=True)),
                ('Learner_branch_name', models.CharField(blank=True, default='Pune', max_length=100, null=True)),
                ('counsellor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('guardian_name', models.CharField(blank=True, max_length=100, null=True)),
                ('guardian_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('relation_with_guardian', models.CharField(blank=True, max_length=100, null=True)),
                ('additional_information', models.TextField(blank=True, null=True)),
                ('program_name', models.CharField(blank=True, max_length=100, null=True)),
                ('admission_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('domain_name', models.CharField(blank=True, max_length=100, null=True)),
                ('communication_mock', models.CharField(blank=True, default='PENDING', max_length=100, null=True)),
                ('technical_mock', models.CharField(blank=True, default='PENDING', max_length=100, null=True)),
                ('latest_qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('latest_pass_out_year', models.CharField(blank=True, max_length=10, null=True)),
                ('tenth_pass_out_year', models.CharField(blank=True, max_length=10, null=True)),
                ('tenth_percentage_cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('tenth_percentage_cgpa_range', models.CharField(blank=True, max_length=100, null=True)),
                ('twelfth_or_diploma', models.CharField(blank=True, max_length=100, null=True)),
                ('twelfth_pass_out_year', models.CharField(blank=True, max_length=10, null=True)),
                ('twelfth_percentage_cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('twelfth_percentage_cgpa_range', models.CharField(blank=True, max_length=100, null=True)),
                ('diploma_pass_out_year', models.CharField(blank=True, max_length=10, null=True)),
                ('diploma_percentage_cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diploma_percentage_cgpa_range', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_pass_out_year', models.CharField(blank=True, max_length=10, null=True)),
                ('graduation_percentage_cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('graduation_percentage_cgpa_range', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_cgpa_range', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_pass_out_year', models.CharField(blank=True, max_length=10, null=True)),
                ('post_graduation_percentage_cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('educational_gap', models.CharField(blank=True, default='NO', max_length=100, null=True)),
                ('fresher_experienced', models.CharField(blank=True, default='Fresher', max_length=100, null=True)),
                ('experience_in_which_technology', models.CharField(blank=True, max_length=255, null=True)),
                ('years_of_experience', models.PositiveIntegerField(blank=True, default=0.0, null=True)),
                ('employment_details', models.TextField(blank=True, null=True)),
                ('last_current_ctc', models.BigIntegerField(blank=True, default=0.0, null=True)),
                ('employment_gap', models.CharField(blank=True, max_length=10, null=True)),
                ('skillset', models.TextField(blank=True, null=True)),
                ('candidate_status', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate_performance', models.CharField(choices=[('good', 'Good'), ('average', 'Average'), ('poor', 'Poor')], default='not updated', max_length=20)),
                ('notice_period', models.CharField(blank=True, default='Immediate Join', max_length=50, null=True)),
                ('upload_resume', models.FileField(blank=True, null=True, upload_to='resume/')),
                ('course_duration', models.CharField(blank=True, default='6 Months', max_length=100, null=True)),
                ('trainer_remarks', models.TextField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='myapp_user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='myapp_user_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
