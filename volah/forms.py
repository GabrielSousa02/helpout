from django import forms


from .models import Volunteer, Organization


class DateInput(forms.DateInput):
    input_type = "date"


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

        labels = {
            "name": "*Organization's Name",
            "legal_status": "*Org. Legal Status",
            "hq_country": "*Headquarters's Country",
            "hq_state_province": "*Headquarters's State/Province",
            "address_line_1": "*Address Line 1",
            "phone": "*Org. Phone",
        }


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = "__all__"

        widgets = {
            "date_of_birth": DateInput(),
        }

        labels = {
            "name": "*First Name",
            "surname": "*Last Name",
            "date_of_birth": "*Date of Birth",
            "email": "*Email",
            "phone": "*Phone",
            "country": "*Country",
            "state_province": "*State/Province",
        }
