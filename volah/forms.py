from django import forms


from .models import Volunteer, Organization


class DateInput(forms.DateInput):
    input_type = 'date'


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

        labels = {
            'hq_country': 'Headquarters Country',
            'hq_state_province': 'Headquarters State/Province'
        }


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'

        widgets = {
            'date_of_birth': DateInput(),
        }

        labels = {
            'name': '*First Name',
            'surname': '*Last Name',
            'date_of_birth': '*Date of Birth',
            'email': '*Email',
            'phone': '*Phone',
            'country': '*Country',
            'state_province': '*State/Province',
        }
