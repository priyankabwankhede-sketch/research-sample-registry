from django.db import models

class Sample(models.Model):
    SAMPLE_TYPES = [
        ('Blood', 'Blood'),
        ('Plasma', 'Plasma'),
        ('CSF', 'CSF'),
    ]

    STATUS_CHOICES = [
        ('Collected', 'Collected'),
        ('Processing', 'Processing'),
        ('Stored', 'Stored'),
        ('Archived', 'Archived'),
    ]

    sample_id = models.CharField(max_length=50, unique=True)
    subject_id = models.CharField(max_length=50)
    sample_type = models.CharField(max_length=20, choices=SAMPLE_TYPES)
    collection_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.sample_id} - {self.sample_type}"
