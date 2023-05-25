"""User model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class User(AbstractUser):
    """ User model
    Extend from Django's Abstract User, change the username field
    to phone and add some extra fields.
    """
    email = models.EmailField('email address', unique=True, error_messages={'unique': 'A user with that email already exists.'})
    
    phone_regex = RegexValidator(regex=r'\+?1?\d{9,10}$', message="Phone number must be entered in the format: +999999999. Up to 10 digits allowed.")
    phone_number = models.CharField('phone', validators=[phone_regex], max_length=10, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']
    is_verified = models.BooleanField('verified', default=True, help_text='Set to true when the user have verified its email address.')

    ROLES_CHOICES = [(0, 'Admin'),]
    role = models.IntegerField(choices=ROLES_CHOICES, default=0)

    TYPE_DOCUMENT_CHOICES = [(0, 'Cedula Ciudadania'),]
    type_document = models.IntegerField(choices=TYPE_DOCUMENT_CHOICES, default=0)

    number_document = models.IntegerField('Número documento', default=0)
    
    created_at = models.DateTimeField('created at', auto_now_add=True, help_text='Date time on which the object was created.')
    modified_at = models.DateTimeField('modified at', auto_now=True, help_text='Date time on which the object was last modified.')

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username

    def clean(self):
        if self.phone_number != '':
            if not validateUniquePhoneNumber(self):
               raise ValidationError({ "error": True, "errorMsg": ["Error, telefono ya esta registrado"] })

def validateUniquePhoneNumber(model):
    users = User.objects.filter(phone_number=model.phone_number)

    if len(users):
        for user in users:
            if user.email != model.email:
                return False

    return True
