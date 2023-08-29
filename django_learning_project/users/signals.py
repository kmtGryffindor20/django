from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from users.models import Profile

# Here we define a something similar to a trigger in SQL.
# For this we need to receive a signal from another table that a value has beed inserted.

# We define that this trigger will be ON INSERT by saying post_save
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # The sender is the model/table from where the signal is coming from.
    # The instance is the new entry in that model.
    # created is a boolean for it being created or not.

    # All this passes to the decorator of receiver and the instance is returned from the User model
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # We save the profile of the User instance in the Profile Model when the User has been saved in the User model
    instance.profile.save()