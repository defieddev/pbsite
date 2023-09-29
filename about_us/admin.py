from django.contrib import admin
from django.shortcuts import render, redirect
from .models import ParishianClub, ClubMembers, Announcements, Profile, Profpic, Birthday, Occupation, Year_Joined, Height, Weight, Age, JerseyNumPic, TinNum, GcashNum, Team, JerseyNum
# from django.contrib.admin.models import LogEntry
# from .forms import CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User

admin.site.register(Profile)
admin.site.register(Profpic)
admin.site.register(Birthday)
admin.site.register(Occupation)
admin.site.register(Year_Joined)
admin.site.register(Height)
admin.site.register(Weight)
admin.site.register(Age)
admin.site.register(JerseyNumPic)
admin.site.register(TinNum)
admin.site.register(GcashNum)
admin.site.register(JerseyNum)
admin.site.register(Team)

class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(DefaultUserAdmin):
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# admin.site.register(LogEntry)
@admin.register(ParishianClub)
class ParishianClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# class CustomUserProfileAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Profile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'birthday', 'contact_no', 'profile_picture', 'occupation', 'address')
# admin.site.unregister(UserProfile)
# admin.site.register(UserProfile, CustomUserProfileAdmin)

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

# class CustomUserAdmin(UserAdmin):
#     form = CustomUserChangeForm
#     model = User
#     list_display = ['username', 'email', 'first_name', 'last_name', 'birthday', 'contact_no', 'occupation', 'address']

# admin.site.register(User, CustomUserAdmin)
