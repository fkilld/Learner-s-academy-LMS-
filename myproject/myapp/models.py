from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.core.validators import FileExtensionValidator
import datetime

ROLE_CHOICES = [
    ('student', 'Student'),
    ('trainer', 'Trainer'),
    ('admin', 'Admin'),
]

CLASS_MODE_CHOICES = [
    ('offline', 'Offline'),
    ('online', 'Online'),
    ('hybrid', 'Hybrid'),
]

STATUS_CHOICES = [
    ('not completed', 'Not Completed'),
    ('pass', 'Pass'),
    ('fail', 'Fail'),
    ('canceled', 'Canceled'),
]

PERFORMANCE_CHOICES = [
    ('good', 'Good'),
    ('average', 'Average'),
    ('poor', 'Poor'),
]

class CustomUserManager(BaseUserManager): 
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    
    groups = models.ManyToManyField(
        Group,
        related_name='myapp_user_set',  # Add related_name here
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='myapp_user_set',  # Add related_name here
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    
    email = models.EmailField(
        max_length=254, unique=True, db_index=True, primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    middle_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_picture = models.ImageField(upload_to='user_profile_pics/', null=True, blank=True, validators=[
                                        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    alternate_phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    landmark = models.CharField(max_length=255, null=True, blank=True)
    locality = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=25, null=True, blank=True)
    state = models.CharField(max_length=50, null=True,
                             default='Maharashtra', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=25, null=True, blank=True)
    linkedin_id = models.CharField(max_length=255, null=True, blank=True)
    github_id = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    class_mode = models.CharField(
        max_length=100, choices=CLASS_MODE_CHOICES, null=True, blank=True)
    
    Learner_branch_name = models.CharField(
        max_length=100, default='Pune', null=True, blank=True)
    
    counsellor_name = models.CharField(max_length=100, null=True, blank=True)
    
    guardian_name = models.CharField(max_length=100, null=True, blank=True)
    
    guardian_phone = models.CharField(max_length=20, null=True, blank=True)
    
    relation_with_guardian = models.CharField(
        max_length=100, null=True, blank=True)
    
    additional_information = models.TextField(null=True, blank=True)
    
    program_name = models.CharField(max_length=100, null=True, blank=True)
    
    admission_date = models.DateField(
        null=True, default=datetime.date.today, blank=True)
    
    domain_name = models.CharField(max_length=100, null=True, blank=True)
    
    communication_mock = models.CharField(
        max_length=100, null=True, default='PENDING', blank=True)
    
    technical_mock = models.CharField(
        max_length=100, default='PENDING', null=True, blank=True)
    
    latest_qualification = models.CharField(
        max_length=100, null=True, blank=True)
    
    latest_pass_out_year = models.CharField(
        null=True, blank=True, max_length=10)
    
    tenth_pass_out_year = models.CharField(
        null=True, blank=True, max_length=10)
    
    tenth_percentage_cgpa = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    
    tenth_percentage_cgpa_range = models.CharField(
        max_length=100, null=True, blank=True)

    twelfth_or_diploma = models.CharField(
        max_length=100, null=True, blank=True)

    twelfth_pass_out_year = models.CharField(
        null=True, blank=True, max_length=10)
    
    twelfth_percentage_cgpa = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    
    twelfth_percentage_cgpa_range = models.CharField(
        max_length=100, null=True, blank=True)

    diploma_pass_out_year = models.CharField(
        null=True, blank=True, max_length=10)
    
    diploma_percentage_cgpa = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    
    diploma_percentage_cgpa_range = models.CharField(
        max_length=100, null=True, blank=True)


    graduation = models.CharField(max_length=100, null=True, blank=True)
    
    graduation_pass_out_year = models.CharField(
        null=True, blank=True, max_length=10)
    
    graduation_percentage_cgpa = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    
    graduation_percentage_cgpa_range = models.CharField(
        max_length=100, null=True, blank=True)

    post_graduation = models.CharField(max_length=100, null=True, blank=True)
    
    post_graduation_cgpa_range = models.CharField(
        max_length=100, null=True, blank=True)
    
    post_graduation_pass_out_year = models.CharField(
        null=True, blank=True, max_length=10)
    
    post_graduation_percentage_cgpa = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)

    educational_gap = models.CharField(
        max_length=100, default="NO", null=True, blank=True)
    
    fresher_experienced = models.CharField(
        max_length=100, null=True, blank=True, default='Fresher')
    
    experience_in_which_technology = models.CharField(
        max_length=255, null=True, blank=True)
    
    years_of_experience = models.PositiveIntegerField(
        null=True, default=0.0, blank=True)
    
    employment_details = models.TextField(null=True, blank=True)
    
    last_current_ctc = models.BigIntegerField(
        null=True, default=0.0, blank=True)
    
    employment_gap = models.CharField(null=True, blank=True, max_length=10)
    
    skillset = models.TextField(null=True, blank=True)
    candidate_status = models.CharField(max_length=50, null=True, blank=True)
    
    candidate_performance = models.CharField(
        max_length=20, choices=PERFORMANCE_CHOICES, default='not updated')
    
    notice_period = models.CharField(
        max_length=50, default='Immediate Join', null=True, blank=True)
    
    upload_resume = models.FileField(
        upload_to='resume/', null=True, blank=True)
    
    course_duration = models.CharField(
        max_length=100, default='6 Months', null=True, blank=True)
    trainer_remarks = models.TextField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role}) - {self.email}"
