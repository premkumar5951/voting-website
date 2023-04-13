from django.contrib import admin
from .models import ElectionParties,ElectionEvents, PartyVotes, UserVotes

# Register your models here.
@admin.register(ElectionParties)
class ElectionPartiesAdmin(admin.ModelAdmin):
    list_display = ('name','manifesto','candidate_name', 'logo','created_at')
    search_fields = ('name','candidate_name')
    
    
    
@admin.register(ElectionEvents)
class ElectionEventsAdmin(admin.ModelAdmin):
    list_display = ('name','is_started','is_ongoing', 'is_ended','created_by','event_date','created_at','event_end_date')
    search_fields = ('name',)
    
    
@admin.register(PartyVotes)
class PartyVotesAdmin(admin.ModelAdmin):
    list_display = ('party','event_name','created_at')
    search_fields = ('event',)
    
    @admin.display(description='Event name')
    def event_name(self, object):
        return object.event.name
    
@admin.register(UserVotes)
class UserVotesAdmin(admin.ModelAdmin):
    list_display = ('user','event_name','created_at')
    search_fields = ('event',)
    
    @admin.display(description='Event name')
    def event_name(self, object):
        return object.event.name