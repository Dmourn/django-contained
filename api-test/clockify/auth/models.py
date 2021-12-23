from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User

class ClockifyWebhook(models.Model):
    key=models.CharField(max_length=64)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE, primary_key=True)
    #user=models.ForeignKey(User, on_delete=models.CASCADE)

    #webhooksecret=models.CharField(max_length=64)
    #webhooksecret=models.OneToOneField(User, on_delete=models.CASCADE)
    """
#class ClockifyWebhook(AbstractUser):
    USERNAME_FIELD = 'webhooksecret'
    #REQUIRED_FIELDS = []
    def has_perm(self, perm, obj=None):
        #Always Yes
        return True
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    """
