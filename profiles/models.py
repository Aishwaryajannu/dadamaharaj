from django.db import models
from django.utils.text import slugify
import qrcode
from io import BytesIO
from django.core.files import File

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.SlugField(unique=True, blank=True)  # New field for clean URL
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    linkedin = models.URLField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = slugify(self.full_name)
        super().save(*args, **kwargs)
        qr_url = f"http://localhost:5173/{self.username}/"
        qr = qrcode.make(qr_url)

        # Save image to memory buffer
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        file_name = f'{self.username}_qr.png'

        # Save to the ImageField without prompting
        self.qr_code.save(file_name, File(buffer), save=False)

        # Now save again with QR image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
