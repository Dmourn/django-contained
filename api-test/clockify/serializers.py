from django.contrib.auth.models import User, Group
from rest_framework import serializers, permissions 

from django.core.validators import EmailValidator

from .models import  Accounts, Contacts, ClockifyClient, ClockifyTimeEntry, ClockifyProject

from .fields import ClockifyClientField, TimeIntervalField, ClockifyProjectField, ClockifyUserField

import datetime



class ContactsSerializer(serializers.Serializer):
    contact_id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100, validators=[EmailValidator()])
    account = serializers.PrimaryKeyRelatedField(queryset=Accounts.objects.all(), read_only=False, required=False)

    def create(self, validated_data):
        return Contacts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.contact_id = validated_data.get('contact_id', instance.contact_id)
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.account_id = validated_data.get('account_id', instance.account_id)
        instance.account_name = validated_data.get('account_name', instance.account_name)
        instance.save()
        return instance
        
"""
class AccountsSerializer(serializers.Serializer):
    account_id = serializers.IntegerField()
    account_name = serializers.CharField(max_length=100)
    contact = ContactsSerializer(source='account',many=True, required=False)

    def create(self, validated_data):
        return Accounts.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.account_name = validated_data.get('account_name',instance.account_name)
        instance.account_id = validated_data.get('account_id',instance.account_id)
        instance.save()
        return instance
"""

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClockifyProject
        fields = [
        'account_id',
        'account_name',
        ]
        read_only_fields = ['client']
        depth=1

class ClockifyClientSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    workspaceId = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=200, required=False, allow_null=True)
    #archived = serializers.CharField(max_length=50000000000)
    archived = serializers.BooleanField()

    def create(self, validated_data):
        return ClockifyClient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id',instance.id)
        instance.name = validated_data.get('name',instance.name)
        instance.workspaceId = validated_data.get('workspaceId',instance.workspaceId)
        instance.address = validated_data.get('address',instance.address)
        instance.archived = validated_data.get('archived',instance.archived)
        instance.save()
        return instance

class ClockifyProjectSerializer(serializers.ModelSerializer):
    client = ClockifyClientField(source="*")
    class Meta:
        model = ClockifyProject
        fields = [
        'id',
        'name',
        'client',
        'workspaceId',
        'billable',
        ]
        read_only_fields = ['client']
        depth=1


class ClockifyTimeEntrySerializer(serializers.ModelSerializer):
    #timeint = ClockifyTimeIntervalSerializer()
    #timeInterval = serializers.CharField(source='data["timeInterval"]')
    timeInterval = TimeIntervalField(source='*')
    project = ClockifyProjectField(source='*')
    user = ClockifyUserField(source='*')
    class Meta:
        model = ClockifyTimeEntry
        fields = [
            'id',
            'description',
            'user',
            'billable',
            'project',
            'timeInterval',
        ]
        read_only_fields = ['project','user']
        depth=2

    """
    def create(self, validated_data):
        timeint_data = validated_data.pop('timeInterval')
        ClockifyTimeEntry.objects.creat(**validated_data)
        ClockifyTimeInterval.objects.create(,**timeint_data)
    """

