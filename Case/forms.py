# forms.py

from django import forms
from .models import Contact,Case

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['type', 'first_name', 'last_name', 'phone', 'email', 'address']
        widgets = {
            'type': forms.Select(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'first_name': forms.TextInput(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'last_name': forms.TextInput(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'phone': forms.TextInput(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'email': forms.EmailInput(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'address': forms.TextInput(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
        }


class EmailForm(forms.Form):
    contact = forms.ModelChoiceField(queryset=Contact.objects.all(), 
                                     empty_label="-----------", 
                                     label="Contact",
                                             widget=forms.Select(attrs={
                                            'class': 'form-select mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
                                            }))
    
class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['insurer', 'insurer_ref', 'client', 'client_ref', 'claimant', 'insured', 'case_type']
        widgets = {
            'case_type': forms.Select(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'insurer': forms.Select(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'insurer_ref': forms.TextInput(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'client': forms.Select(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'client_ref': forms.TextInput(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'claimant': forms.TextInput(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'insured': forms.TextInput(attrs={'class': 'block w-full mt-1 rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            }