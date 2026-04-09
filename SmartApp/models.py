from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage
class IncidentReport(models.Model):
    REPORT_TYPES = [
        ('safety', 'Safety'), ('waste', 'Waste'),
        ('water', 'Water'), ('air', 'Air'), ('lost', 'Lost')
    ]
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    category = models.CharField(max_length=100)
    urgency = models.CharField(max_length=20, default='Medium')
    description = models.TextField()
    evidence = models.ImageField(upload_to='reports/',storage=MediaCloudinaryStorage(), null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.category} - {self.status}"