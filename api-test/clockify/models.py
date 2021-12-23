import datetime
from django.db import models

#class ClockifyWebhook(models.Model):
#webhooksecret=models.CharField(max_length=64)

class ClockifyClient(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=100)
    workspaceId = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    archived = models.BooleanField(default=False)

class ClockifyProject(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=100)
    clientId = models.ForeignKey(ClockifyClient, related_name='client', on_delete=models.PROTECT)
    #clientId = models.OneToOneField(ClockifyClient, related_name='client', on_delete=models.PROTECT)
    workspaceId = models.CharField(max_length=100)
    billable = models.BooleanField(default=False)


class ClockifyTimeEntry(models.Model):
    #timeId = models.CharField(max_length=64, primary_key=True)
    id = models.CharField(max_length=64, primary_key=True)
    description = models.TextField(max_length=500, blank=True)
    userId = models.CharField(max_length=64) # FOREIGN KEY
    billable = models.BooleanField(default=False)
    projectId = models.CharField(max_length=64) #FOREIGN KEY
    start = models.DateTimeField()
    end = models.DateTimeField()
    duration = models.DurationField()
    #timeInterval = models.OneToOneField(ClockifyTimeInterval, related_name='wtf', on_delete=models.CASCADE)

    def eval_time(self):
        start = datetime.datetime.fromisoformat(self.timeInterval['start'][:-1])
        end = datetime.datetime.fromisoformat(self.timeInterval['end'][:-1])
        self.delta = end - start
        return self.delta


class Accounts(models.Model):
    account_id = models.BigIntegerField(primary_key=True)
    account_name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(f'{self.account_name} : {self.account_id}')

class Contacts(models.Model):
    contact_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    account = models.ForeignKey('Accounts', related_name='contact', on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.first_name} : {self.last_name}')
