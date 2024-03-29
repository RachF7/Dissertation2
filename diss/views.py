from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.http import HttpResponse
import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from .models import Location, forum

from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from diss.forms import UserForm, UserProfileForm, CreateInDiscussion, CreateInForum

from django.contrib.auth import login
from django.contrib import messages


def index(request):
    context_dict = {}
    return render(request, 'diss/index2.html', context=context_dict)




from .models import Location


def map(request):
    location_list = list(Location.objects.order_by('name').values())
    location_json = json.dumps(location_list)
    context = {'locations': location_json}
    return render(request, 'diss/map.html', context)


def events(request):
    context_dict = {}
    return render(request, 'diss/events.html', context=context_dict)


class MarkersMapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["location"] = json.loads(serialize("geojson", Location.objects.all()))
        return context


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'diss/register.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('diss:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'diss/login.html')


@login_required
def restricted(request):
    return render(request, 'diss/restricted.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('diss:index'))


def chat(request):
    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'diss/chat.html', context)


def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'diss/addInForum.html', context)


def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'diss/addInDiscussion.html', context)
