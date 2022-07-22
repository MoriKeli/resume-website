from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from resume.models import Profile

@receiver(post_save, sender=User)
def create_personal_profile(sender, instance, created, **kwargs):
    if created:
        print('Instance: ', instance)
        if instance.is_staff == True and instance.is_superuser == True:
            Profile.objects.create(user=instance)