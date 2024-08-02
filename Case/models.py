from django.db import models
from django.utils import timezone

class Case(models.Model):
    CASE_TYPE_CHOICES = [
        ('1', 'WC'),
        ('2', 'CTP'),
    ]

    CLIENT_TYPE_CHOICES = [
        ('Procare', 'Procare'),
        ('Worksite', 'Worksite'),
    ]

    INSURER_TYPE_CHOICES = [
        ('EML', 'EML'),
        ('Allianz', 'Allianz'),
        ('Suncorp', 'Suncorp'),
    ]

    insurer = models.CharField(max_length=100, choices=INSURER_TYPE_CHOICES)
    insurer_ref = models.CharField(max_length=255)
    client = models.CharField(max_length=100, choices=CLIENT_TYPE_CHOICES)
    client_ref = models.CharField(max_length=255)
    claimant = models.CharField(max_length=255)
    insured = models.CharField(max_length=255)
    case_type = models.CharField(max_length=50, choices=CASE_TYPE_CHOICES)

    def __str__(self):
        return f'{self.client}-{self.insurer}'


class Contact(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE,related_name='contact')
    CONTACT_TYPE_CHOICES = [
    ('Claimant', 'Claimant'),
    ('Insured', 'Insured'),
    ('Employer_Contact', 'Employer Contact'),
    ('Witness', 'Witness'),
    ('Client_Contact', 'Client Contact'),
    ('Other', 'Other'),
        # Add more contact types as needed
    ]

    type = models.CharField(max_length=100, choices=CONTACT_TYPE_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=255)
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Note(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.note[:50]  
    
class EmailTemplate(models.Model):
    note = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.note[:50]


