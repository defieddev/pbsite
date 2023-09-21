from django.contrib import admin
from django.shortcuts import render, redirect
from .models import ParishianClub, ClubMembers, Announcements
# from django.contrib.admin.models import LogEntry
# from .forms import CustomLogEntry

# admin.site.register(LogEntry)
@admin.register(ParishianClub)
class ParishianClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(ClubMembers)
class ParishianClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_joined')

@admin.register(Announcements)
class ParishianClubAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        initial['user'] = request.user.id  # Set the user initially to the current user
        return initial
    list_display = ('title', 'description', 'picture', 'date_created')





