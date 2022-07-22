from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp = models.ImageField(upload_to='MoriKeliDps/', default='default.jpg')
    bio = models.TextField(max_length=500)
    estate = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=14)
    facebook_link = models.URLField()
    instagram_link = models.URLField()
    twitter_link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        image = Image.open(self.dp.path)
        if image.height > 500 and image.width > 500:
            output_size = (500, 500)
            image.thumbnail(output_size)
            image.save(self.dp.path)

    class Meta:
        verbose_name_plural = 'Profile'
        
    def __str__(self):
        return f'{self.user}'
    
class Resume(models.Model):
    resume_obj = models.ForeignKey(Profile, on_delete=models.CASCADE)
    university = models.CharField(max_length=30)
    university_desc = models.TextField()
    university_degree = models.CharField(max_length=50)
    high_school = models.CharField(max_length=30)
    highsch_desc = models.TextField()
    
    def __str__(self):
        return self.resume_obj

class Portofolio(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    port = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=70, blank=False)
    description = models.TextField(blank=False)
    category = models.CharField(max_length=100, choices=(('Art', 'Art'), ('Python Program', 'Python Program'), ('Web development', 'Web development')))
    project_thumbnail = models.ImageField(upload_to='Portofolio Thumbnails/')
    github_link = models.URLField(blank=False)
    posted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Portofolio, self).save(*args, **kwargs)

        image = Image.open(self.project_thumbnail.path)
        if image.height > 800 and image.width > 700:
            output_size = (800, 800)
            image.thumbnail(output_size)
            image.save(self.project_thumbnail.path)

    class Meta:
        verbose_name_plural = 'Portofolio'

    def __str__(self):
        return f'{self.project_name}'
    