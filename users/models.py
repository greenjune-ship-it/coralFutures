from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # Resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        # Crop the image to a square shape
        size = min(img.width, img.height)
        left = (img.width - size) // 2
        top = (img.height - size) // 2
        right = left + size
        bottom = top + size
        img = img.crop((left, top, right, bottom))

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

