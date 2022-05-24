from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView


from .models import Volunteer, Organization
from .forms import VolunteerForm, OrganizationForm
# Create your views here.


class VolahHomeTemplateView(TemplateView):
    template_name = 'volah/volah_home.html'


def create_volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('volah:volah_home'))
    else:
        form = VolunteerForm()
    return render(request, 'volah/volunteer_form.html', context={'form': form})


class VolunteerListView(ListView):
    model = Volunteer
    context_object_name = 'volunteers_list'


class VolunteerDetailView(DetailView):
    model = Volunteer


class VolunteerUpdateView(UpdateView):
    model = Volunteer
    success_url = reverse_lazy('volah:list_volunteer')
    fields = '__all__'


class VolunteerDeleteView(DeleteView):
    model = Volunteer
    success_url = reverse_lazy('volah:list_volunteer')


def create_organization(request):

    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('volah:volah_home'))
    else:
        form = OrganizationForm()
    return render(request, 'volah/organization_form.html', context={'form': form})


class OrganizationListView(ListView):
    model = Organization
    context_object_name = 'organizations_list'


class OrganizationDetailView(DetailView):
    model = Organization


class OrganizationUpdateView(UpdateView):
    model = Organization
    success_url = reverse_lazy('volah:list_organization')
    fields = '__all__'


class OrganizationDeleteView(DeleteView):
    model = Organization
    success_url = reverse_lazy('volah:list_organization')

