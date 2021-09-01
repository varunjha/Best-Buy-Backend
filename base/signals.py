from django.db.models.signals import pre_save
from django.contrib.auth.models import User

# The signals will make username, the email of the user.
def updateUser(sender, instance, **kwargs):
    user = instance
    if user.email != '':
        user.username = user.email


pre_save.connect(updateUser, sender=User)
