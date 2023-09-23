from django.shortcuts import render, redirect, get_object_or_404
from .models import ParishianClub, ClubMembers, Announcements
from django.contrib.auth.forms import UserCreationForm
# from django_registration.backends.activation.views import RegistrationView
from django.urls import reverse_lazy
from django.views import generic
from .forms import AnnouncementsForm, CustomRegistrationForm
# from django.core.mail import send_mail
from django.conf import settings
from random import shuffle
from django.core.paginator import Paginator

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

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# class CustomRegistrationView(RegistrationView):
#     form_class = CustomRegistrationForm

#     def register(self, form):
#         user = form.save(commit=False)
#         user.is_active = False # set user as inactive initially
#         user.save()

#         # sending email notif to admin
#         subject = 'Approval of New Member Registration'
#         message = f'Greetings. This is auto-generated. A new member has sent approval for request to be registered. Username: {user.username}'
#         from_email = settings.DEFAULT_FROM_EMAIL
#         recipient_list = [settings.azurathecookie34@gmail.com]
#         send_mail(subject, message,from_email, recipient_list)

#         return user

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