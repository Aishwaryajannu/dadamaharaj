import os
import qrcode
from django.db import models
from django.conf import settings
from io import BytesIO
from django.core.files import File

class Profile(models.Model):
    username = models.SlugField(unique=True)
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    linkedin = models.CharField(max_length=100)
    location = models.TextField()
    image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def get_profile_url(self):
        return f"http://localhost:5173/{self.username}/"

    def generate_qr(self):
        url = self.get_profile_url()
        qr = qrcode.make(url)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        filename = f"{self.username}_qr.png"
        filebuffer = File(buffer, name=filename)
        self.qr_code.save(filename, filebuffer, save=False)

    def save(self, *args, **kwargs):
    
        if not self.qr_code:
            self.generate_qr()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
