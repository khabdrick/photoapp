from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.contrib import auth

class User(auth.models.User,auth.models.PermissionsMixin):
    image=models.ImageField(upload_to='profile_image',blank=True)
    def __str__(self):
        '@{}'.format(self.username)
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})
    
        
