from django.shortcuts import render, redirect, get_object_or_404
from .models import ParishianClub, ClubMembers, Announcements, Profpic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
# from django_registration.backends.activation.views import RegistrationView
from django.urls import reverse_lazy
from django.views import generic
from .forms import AnnouncementsForm, CustomRegistrationForm, ProfpicForm, BirthdayForm, OccupationForm, YearJoinedForm, HeightForm, WeightForm, AgeForm, JerseyNumPicForm, TinNumForm, JerseyNumForm, GcashNumForm, TeamForm
# from django.core.mail import send_mail
from django.conf import settings
from random import shuffle
from .models import Profpic, Birthday, Occupation, Year_Joined, Height, Weight, Age, JerseyNumPic
# from .forms import CustomUserChangeForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User

def about_us(request):
    club = ParishianClub.objects.first()
    announcements = Announcements.objects.all()
    return render(request, 'about_us/about_us.html', {'club': club, 'announcements': announcements})

def members(request):
    members = ClubMembers.objects.all()
    return render(request, 'members/members.html', {'members': members})

def announcements(request):
    announcements = Announcements.objects.all()
    return render(request, 'announcements/announcements.html', {'announcements': announcements})

def logout_view(request):
    logout(request)
    return redirect('about_us')

class SignUp(generic.CreateView):
    success_url = 'login'
    form_class = CustomRegistrationForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

## CLASS VIEWS
@login_required
def profile_view(request):
    user = request.user
    profpic, created = Profpic.objects.get_or_create(user=user)  # Retrieve or create the profpic object for the current user
    if request.method == 'POST':
        form = ProfpicForm(request.POST, request.FILES, instance=profpic)
        if form.is_valid():
            profpic = form.save(commit=False)
            profpic.user = user
            profpic.save()
            return redirect('profile')
    else:
        form = ProfpicForm(instance=profpic)
    return render(request, 'profile/profile.html', {'user': user, 'form': form, 'profpic': profpic})

# @login_required
# def jerseynum_view(request):
#     user = request.user
#     jerseynumpic, created = JerseyNumPic.objects.get_or_create(user=user)  # Retrieve or create the jersey number pic object for the current user
#     if request.method == 'POST':
#         form = JerseyNumPicForm(request.POST, request.FILES, instance=jerseynumpic)
#         if form.is_valid():
#             jerseynumpic = form.s

#             jerseynumpic.user = user
#             jerseynumpic.save()
#             return redirect('jerseynum')
#     else:
#         form = JerseyNumPicForm(instance=jerseynumpic)
#     return render(request, 'profile/profile.html', {'user': user, 'form': form, 'jerseynumpic': jerseynumpic})

@login_required
def birthday_view(request):
    user = request.user
    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        if form.is_valid():
            birthday = form.save(commit=False)
            if 'name' in form.cleaned_data:
                birthday.name = form.cleaned_data['name']
            else:
                # Handle the case when 'name' is not present in the form submission
                # You can either set a default value or raise an error
                birthday.name = 'Default Name'
            birthday.user = user
            birthday.save()
            return redirect('profile')
        else:
            # Handle the case when the form is not valid
            # You can redirect to an error page or render the form again with error messages
            return render(request, 'profile/birthday.html', {'form': form, 'error': form.errors})
    else:
        form = BirthdayForm()
    return render(request, 'profile/birthday.html', {'user': user, 'form': form})

    user = request.user
    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        if form.is_valid():
            birthday = form.save(commit=False)
            birthday.name = form.cleaned_data['name']  # Set the name attribute based on the user input
            birthday.user = user
            birthday.save()
            return redirect('profile')
    else:
        form = BirthdayForm()
    return render(request, 'profile/profile.html', {'user': user, 'form': form})

@login_required
def occupation_view(request):
    user = request.user
    if request.method == 'POST':
        form = OccupationForm(request.POST)
        if form.is_valid():
            occupation = form.save(commit=False)
            if 'name' in form.cleaned_data:
                occupation.name = form.cleaned_data['name']
            else:
                occupation.name = 'Default Name'
            occupation.user = user
            occupation.save()
            return redirect('profile')
        else:
            return render(request, 'profile/occupation.html', {'form': form, 'error': form.errors})
    else:
        form = OccupationForm()
    return render(request, 'profile/occupation.html', {'user': user, 'form': form})

@login_required
def height_view(request):
    user = request.user
    if request.method == 'POST':
        form = HeightForm(request.POST)
        if form.is_valid():
            height = form.save(commit=False)
            if 'name' in form.cleaned_data:
                height.name = form.cleaned_data['name']
            else:
                height.name = 'Default Name'
            height.user = user
            height.save()
            return redirect('profile')
        else:
            return render(request, 'profile/height.html', {'form': form, 'error': form.errors})
    else:
        form = HeightForm()
    return render(request, 'profile/height.html', {'user': user, 'form': form})

@login_required
def weight_view(request):
    user = request.user
    if request.method == 'POST':
        form = WeightForm(request.POST)
        if form.is_valid():
            weight = form.save(commit=False)
            if 'name' in form.cleaned_data:
                weight.name = form.cleaned_data['name']
            else:
                weight.name = 'Default Name'
            weight.user = user
            weight.save()
            return redirect('profile')
        else:
            return render(request, 'profile/weight.html', {'form': form, 'error': form.errors})
    else:
        form = WeightForm()
    return render(request, 'profile/weight.html', {'user': user, 'form': form})

@login_required
def age_view(request):
    user = request.user
    if request.method == 'POST':
        form = AgeForm(request.POST)
        if form.is_valid():
            age = form.save(commit=False)
            if 'name' in form.cleaned_data:
                age.name = form.cleaned_data['name']
            else:
                age.name = 'Default Name'
            age.user = user
            age.save()
            return redirect('profile')
        else:
            return render(request, 'profile/age.html', {'form': form, 'error': form.errors})
    else:
        form = AgeForm()
    return render(request, 'profile/age.html', {'user': user, 'form': form})

def tin_view(request):
    user = request.user
    if request.method == 'POST':
        form = TinNumForm(request.POST)
        if form.is_valid():
            tin = form.save(commit=False)
            if 'name' in form.cleaned_data:
                tin.name = form.cleaned_data['name']
            else:
                tin.name = 'Default Name'
            tin.user = user
            tin.save()
            return redirect('profile')
        else:
            return render(request, 'profile/tin.html', {'form': form, 'error': form.errors})
    else:
        form = TinNumForm()
    return render(request, 'profile/tin.html', {'user': user, 'form': form})

def jerseynum_view(request):
    user = request.user
    if request.method == 'POST':
        form = JerseyNumForm(request.POST)
        if form.is_valid():
            jerseynum = form.save(commit=False)
            if 'name' in form.cleaned_data:
                jerseynum.name = form.cleaned_data['name']
            else:
                jerseynum.name = 'Default Name'
            jerseynum.user = user
            jerseynum.save()
            return redirect('profile')
        else:
            return render(request, 'profile/jerseynum.html', {'form': form, 'error': form.errors})
    else:
        form = JerseyNumForm()
    return render(request, 'profile/jerseynum.html', {'user': user, 'form': form})

def gcashnum_view(request):
    user = request.user
    if request.method == 'POST':
        form = GcashNumForm(request.POST)
        if form.is_valid():
            gcashnum = form.save(commit=False)
            if 'name' in form.cleaned_data:
                gcashnum.name = form.cleaned_data['name']
            else:
                gcashnum.name = 'Default Name'
            gcashnum.user = user
            gcashnum.save()
            return redirect('profile')
        else:
            return render(request, 'profile/gcashnum.html', {'form': form, 'error': form.errors})
    else:
        form = GcashNumForm()
    return render(request, 'profile/gcashnum.html', {'user': user, 'form': form})

def team_view(request):
    user = request.user
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            if 'name' in form.cleaned_data:
                team.name = form.cleaned_data['name']
            else:
                team.name = 'Default Name'
            team.user = user
            team.save()
            return redirect('profile')
        else:
            return render(request, 'profile/team.html', {'form': form, 'error': form.errors})
    else:
        form = TeamForm()
    return render(request, 'profile/team.html', {'user': user, 'form': form})


# end class views

def members_view(request):
    members = User.objects.all()
    context = {
        'members': members,
        'profpics': Profpic.objects.all(),
        'birthdays': Birthday.objects.all(),
        'occupations': Occupation.objects.all(),
        'heights': Height.objects.all(),
        'weights': Weight.objects.all(),
        'ages': Age.objects.all(),
    }
    return render(request, 'members/members.html', context)


def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about_us')
    else:
        form = AnnouncementsForm()
    return render(request, 'announcements/create_post.html', {'form': form})

def announcement_detail(request, announcement_id):
    announcement = get_object_or_404(Announcements, id=announcement_id)
    announcements = list(Announcements.objects.all())
    shuffle(announcements)  # randomizing posts
    paginator = Paginator(announcements, 3)  # show 3 posts per post_detail page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    club = ParishianClub.objects.first()
    return render(request, 'announcements/post_detail.html', {'announcement': announcement, 'club': club, 'page_obj': page_obj})

def search(request):
    query = request.GET.get('q')
    announcements = Announcements.objects.filter(title__icontains=query)
    return render(request, 'about_us/about_us.html', {'announcements': announcements})
