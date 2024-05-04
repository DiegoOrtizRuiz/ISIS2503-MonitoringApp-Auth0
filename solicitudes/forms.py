from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'name',
            'email',
            'phone',
            'id_number',
            'address',
            'city',
            'state',
            'zip_code',
            'country',

        ]
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'id_number': 'ID Number',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'zip_code': 'Zip Code',
            'country': 'Country',
        }