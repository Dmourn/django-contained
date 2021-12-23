from rest_framework import serializers
import datetime

class TimeIntervalField(serializers.Field):
    def to_representation(self, value):
        ret = {
            "start": value.start,
            "end": value.end,
            "duration": value.duration
        }
        return ret
    
    def to_internal_value(self, data):
        ret = {
        "start": datetime.datetime.fromisoformat(data['start'][:-1]),
        "end": datetime.datetime.fromisoformat(data['end'][:-1]),
        "duration": datetime.datetime.fromisoformat(data['end'][:-1])-datetime.datetime.fromisoformat(data['start'][:-1])
        }
        print(datetime.datetime.fromisoformat(data['start'][:-1]).tzinfo)
        return ret

# Field to describe clients from Project creation
class ClockifyClientField(serializers.Field):
    def get_attribute(self, instance):
        # apparently dsomething else gets done by default?
        return instance
        
    #map dict key we want to model value it will have 
    def to_representation(self, value):
        ret = {
        "id": value.client_id,
        #"name": value.name,
        #"address": value.address,
        #"workspaceId": value.workspaceId,
        #"archived": value.archived,
        }
        print(value.__class__.__name__)
        #return value.__class__.__name__
        return ret

    #take value from before, and take it to the internal representation
    def to_internal_value(self, data):
        ret = {
        "client_id": data['id'],
        }
        print(f"custom field data: {data}")
        print(f"returning: {ret}")
        return ret

# field for projects to clients
class ClockifyProjectField(serializers.Field):
    def get_attribute(self, instance):
        return instance
        
    def to_representation(self, value):
        ret = {
        "id": value.project_id,
        }
        return ret

    def to_internal_value(self, data):
        ret = {
        "project_id": data['id'],
        }
        print(f"project data: {data}")
        print(f"returning: {ret}")
        return ret

# flied for clockify user, not auth'd in this system
class ClockifyUserField(serializers.Field):
    def get_attribute(self, instance):
        return instance
        
    def to_representation(self, value):
        ret = {
        "id": value.user_id,
        }
        return ret

    def to_internal_value(self, data):
        ret = {
        "user_id": data['id'],
        }
        print(f"clock-user data: {data}")
        print(f"returning: {ret}")
        return ret
    


