from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.dispatch import receiver


from .models import developer, Company_detail


@receiver(post_save, sender=User)
def post_save_create_job(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance',instance)
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        developer.objects.create(
            user=instance,
            name=instance.username,
            email= instance.email,
            )

        Company_detail.objects.create(
            user=instance,
            Company_name=instance.username,
            Company_Describe= instance.email,
            )
        print('it woring')



