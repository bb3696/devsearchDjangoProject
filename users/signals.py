from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from  django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings


#@receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    print('Profile signal triggered')
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email]
        )



def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        if instance.user:  # 确保 instance.user 不是 None
            instance.user.delete()
    except User.DoesNotExist:
        print("User does not exist, skipping deletion.")
        

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)