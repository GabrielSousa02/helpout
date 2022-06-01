from django.db import models
from django.core.validators import EmailValidator

# Create your models here.


countries = [
    (None, "-"),
    ("afghanistan", "Afghanistan"),
    ("albania", "Albania"),
    ("algeria", "Algeria"),
    ("andorra", "Andorra"),
    ("angola", "Angola"),
    ("antigua_and_barbuda", "Antigua and Barbuda"),
    ("argentina", "Argentina"),
    ("armenia", "Armenia"),
    ("australia", "Australia"),
    ("austria", "Austria"),
    ("azerbaijan", "Azerbaijan"),
    ("bahamas", "Bahamas"),
    ("bahrain", "Bahrain"),
    ("bangladesh", "Bangladesh"),
    ("barbados", "Barbados"),
    ("belarus", "Belarus"),
    ("belgium", "Belgium"),
    ("belize", "Belize"),
    ("benin", "Benin"),
    ("bhutan", "Bhutan"),
    ("bolivia", "Bolivia"),
    ("bosnia_and_herzegovina", "Bosnia and Herzegovina"),
    ("botswana", "Botswana"),
    ("brazil", "Brazil"),
    ("brunei", "Brunei"),
    ("bulgaria", "Bulgaria"),
    ("burkina_faso", "Burkina Faso"),
    ("burundi", "Burundi"),
    ("cote_d'ivoire", "Côte d'Ivoire"),
    ("cabo_verde", "Cabo Verde"),
    ("cambodia", "Cambodia"),
    ("cameroon", "Cameroon"),
    ("canada", "Canada"),
    ("central_african_republic", "Central African Republic"),
    ("chad", "Chad"),
    ("chile", "Chile"),
    ("china", "China"),
    ("colombia", "Colombia"),
    ("comoros", "Comoros"),
    ("congo", "Congo"),
    ("costa_rica", "Costa Rica"),
    ("croatia", "Croatia"),
    ("cuba", "Cuba"),
    ("cyprus", "Cyprus"),
    ("czechia", "Czechia"),
    ("democratic_republic_of_the_congo", "Democratic Republic of the Congo"),
    ("denmark", "Denmark"),
    ("djibouti", "Djibouti"),
    ("dominica", "Dominica"),
    ("dominican_republic", "Dominican Republic"),
    ("ecuador", "Ecuador"),
    ("egypt", "Egypt"),
    ("el_salvador", "El Salvador"),
    ("equatorial_guinea", "Equatorial Guinea"),
    ("eritrea", "Eritrea"),
    ("estonia", "Estonia"),
    ("eswatini", "Eswatini"),
    ("ethiopia", "Ethiopia"),
    ("fiji", "Fiji"),
    ("finland", "Finland"),
    ("france", "France"),
    ("gabon", "Gabon"),
    ("gambia", "Gambia"),
    ("georgia", "Georgia"),
    ("germany", "Germany"),
    ("ghana", "Ghana"),
    ("greece", "Greece"),
    ("grenada", "Grenada"),
    ("guatemala", "Guatemala"),
    ("guinea", "Guinea"),
    ("guinea_bissau", "Guinea-Bissau"),
    ("guyana", "Guyana"),
    ("haiti", "Haiti"),
    ("holy_see", "Holy See"),
    ("honduras", "Honduras"),
    ("hungary", "Hungary"),
    ("iceland", "Iceland"),
    ("india", "India"),
    ("indonesia", "Indonesia"),
    ("iran", "Iran"),
    ("iraq", "Iraq"),
    ("ireland", "Ireland"),
    ("israel", "Israel"),
    ("italy", "Italy"),
    ("jamaica", "Jamaica"),
    ("japan", "Japan"),
    ("jordan", "Jordan"),
    ("kazakhstan", "Kazakhstan"),
    ("kenya", "Kenya"),
    ("kiribati", "Kiribati"),
    ("kuwait", "Kuwait"),
    ("kyrgyzstan", "Kyrgyzstan"),
    ("laos", "Laos"),
    ("latvia", "Latvia"),
    ("lebanon", "Lebanon"),
    ("lesotho", "Lesotho"),
    ("liberia", "Liberia"),
    ("libya", "Libya"),
    ("liechtenstein", "Liechtenstein"),
    ("lithuania", "Lithuania"),
    ("luxembourg", "Luxembourg"),
    ("madagascar", "Madagascar"),
    ("malawi", "Malawi"),
    ("malaysia", "Malaysia"),
    ("maldives", "Maldives"),
    ("mali", "Mali"),
    ("malta", "Malta"),
    ("marshall_islands", "Marshall Islands"),
    ("mauritania", "Mauritania"),
    ("mauritius", "Mauritius"),
    ("mexico", "Mexico"),
    ("micronesia", "Micronesia"),
    ("moldova", "Moldova"),
    ("monaco", "Monaco"),
    ("mongolia", "Mongolia"),
    ("montenegro", "Montenegro"),
    ("morocco", "Morocco"),
    ("mozambique", "Mozambique"),
    ("myanmar (formerly_burma)", "Myanmar (formerly Burma)"),
    ("namibia", "Namibia"),
    ("nauru", "Nauru"),
    ("nepal", "Nepal"),
    ("netherlands", "Netherlands"),
    ("new_zealand", "New Zealand"),
    ("nicaragua", "Nicaragua"),
    ("niger", "Niger"),
    ("nigeria", "Nigeria"),
    ("north_korea", "North Korea"),
    ("north_macedonia", "North Macedonia"),
    ("norway", "Norway"),
    ("oman", "Oman"),
    ("pakistan", "Pakistan"),
    ("palau", "Palau"),
    ("palestine_state", "Palestine State"),
    ("panama", "Panama"),
    ("papua_new_guinea", "Papua New Guinea"),
    ("paraguay", "Paraguay"),
    ("peru", "Peru"),
    ("philippines", "Philippines"),
    ("poland", "Poland"),
    ("portugal", "Portugal"),
    ("qatar", "Qatar"),
    ("romania", "Romania"),
    ("russia", "Russia"),
    ("rwanda", "Rwanda"),
    ("saint_kitts_and_nevis", "Saint Kitts and Nevis"),
    ("saint_lucia", "Saint Lucia"),
    ("saint_vincent_and_the_grenadines", "Saint Vincent and the Grenadines"),
    ("samoa", "Samoa"),
    ("san_marino", "San Marino"),
    ("sao_tome_and_principe", "Sao Tome and Principe"),
    ("saudi_arabia", "Saudi Arabia"),
    ("senegal", "Senegal"),
    ("serbia", "Serbia"),
    ("seychelles", "Seychelles"),
    ("sierra_leone", "Sierra Leone"),
    ("singapore", "Singapore"),
    ("slovakia", "Slovakia"),
    ("slovenia", "Slovenia"),
    ("solomon_islands", "Solomon Islands"),
    ("somalia", "Somalia"),
    ("south_africa", "South Africa"),
    ("south_korea", "South Korea"),
    ("south_sudan", "South Sudan"),
    ("spain", "Spain"),
    ("sri_lanka", "Sri Lanka"),
    ("sudan", "Sudan"),
    ("suriname", "Suriname"),
    ("sweden", "Sweden"),
    ("switzerland", "Switzerland"),
    ("syria", "Syria"),
    ("tajikistan", "Tajikistan"),
    ("tanzania", "Tanzania"),
    ("thailand", "Thailand"),
    ("timor_leste", "Timor-Leste"),
    ("togo", "Togo"),
    ("tonga", "Tonga"),
    ("trinidad_and_tobago", "Trinidad and Tobago"),
    ("tunisia", "Tunisia"),
    ("turkey", "Turkey"),
    ("turkmenistan", "Turkmenistan"),
    ("tuvalu", "Tuvalu"),
    ("uganda", "Uganda"),
    ("ukraine", "Ukraine"),
    ("united_arab_emirates", "United Arab Emirates"),
    ("united_kingdom", "United Kingdom"),
    ("united_states_of_america", "United States of America"),
    ("uruguay", "Uruguay"),
    ("uzbekistan", "Uzbekistan"),
    ("vanuatu", "Vanuatu"),
    ("venezuela", "Venezuela"),
    ("vietnam", "Vietnam"),
    ("yemen", "Yemen"),
    ("zambia", "Zambia"),
    ("zimbabwe", "Zimbabwe"),
]

blood_types = [
    ("", " - "),
    ("a+", "A+"),
    ("a-", "A-"),
    ("b+", "B+"),
    ("b-", "B-"),
    ("ab+", "AB+"),
    ("ab-", "AB-"),
    ("o+", "O+"),
    ("o-", "O-"),
]

skills = [
    ("", "-"),
    ("first_aid", "First Aid"),
    ("comms", "Communications"),
    ("logistics", "Logistics"),
    ("fire_management_suppression", "Fire Management and Suppression"),
    ("search_and_rescue", "Search and Rescue"),
]


class Organization(models.Model):

    name = models.CharField(max_length=250)
    legal_status = models.CharField(max_length=250)
    hq_country = models.CharField(max_length=250, choices=countries)
    hq_state_province = models.CharField(max_length=250)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15)

    org_website = models.URLField(blank=True)
    contact_name = models.CharField(max_length=150, blank=True)
    contact_surname = models.CharField(max_length=150, blank=True)
    contact_phone = models.CharField(max_length=15, blank=True)
    contact_email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Volunteer(models.Model):

    # MANDATORY
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=250, choices=countries)
    state_province = models.CharField(max_length=250)

    # OPTIONAL
    nickname = models.CharField(max_length=100, blank=True)
    blood_type = models.CharField(max_length=5, blank=True, choices=blood_types)
    skills = models.CharField(max_length=250, blank=True, choices=skills)
    organization = models.ForeignKey(
        "Organization", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.name} {self.surname}"
