from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import developer


@receiver(post_save, sender=User)
def post_save_create_job(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance',instance)
    if created:
        developer.objects.create(user=instance)


post_save.connect(post_save_create_job, sender=User)


# @receiver(post_save, sender=User)
# def post_save_company   (sender, instance, created, **kwargs):
#     print('sender', sender)
#     print('instance',instance)
#     if created:
#         test_detail.objects.create(user=instance)

# post_save.connect(post_save_company, sender=User)
        