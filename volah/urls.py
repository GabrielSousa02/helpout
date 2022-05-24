from django.urls import path

from .views import VolahHomeTemplateView
from .views import create_volunteer
from .views import VolunteerListView
from .views import VolunteerDetailView
from .views import VolunteerUpdateView
from .views import VolunteerDeleteView

from .views import create_organization
from .views import OrganizationListView
from .views import OrganizationDetailView
from .views import OrganizationUpdateView
from .views import OrganizationDeleteView


app_name = 'volah'

urlpatterns = [
    # HomePage
    path('', VolahHomeTemplateView.as_view(), name='volah_home'),
    # Volunteer URLs
    path('create_volunteer/', create_volunteer, name='create_volunteer'),
    path('volunteers/', VolunteerListView.as_view(), name='list_volunteer'),
    path('volunteer_detail/<int:pk>', VolunteerDetailView.as_view(), name='volunteer_detail'),
    path('volunteer_update/<int:pk>', VolunteerUpdateView.as_view(), name='volunteer_update'),
    path('volunteer_delete/<int:pk>', VolunteerDeleteView.as_view(), name='volunteer_delete'),
    # Organization URLs
    path('create_organization/', create_organization, name='create_organization'),
    path('organizations/', OrganizationListView.as_view(), name='list_organization'),
    path('organization_detail/<int:pk>', OrganizationDetailView.as_view(), name='organization_detail'),
    path('organization_update/<int:pk>', OrganizationUpdateView.as_view(), name='organization_update'),
    path('organization_delete/<int:pk>', OrganizationDeleteView.as_view(), name='organization_delete'),
]

