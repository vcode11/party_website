import datetime

from django import forms
from django.core.validators import EmailValidator, RegexValidator
from django.forms import CharField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import State, District
from django_select2.forms import ModelSelect2Widget


def validate_date(date):
    """
        Function to validate if a date is not a future date.
    """
    if date > datetime.date.today():
        raise ValidationError(_('Date of Birth can\'t be a future date.'))


class MemberRegistrationForm(forms.Form):
    """
        Form for registration of members.
    """
    name = forms.CharField(label='Name',
                           validators=[RegexValidator(regex=r'([A-Za-z]|\s)+', message='Invalid Characters in name')],
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Name'}
                            )
                           )

    years = (i for i in range(1900,datetime.datetime.today().year+1))
    dob = forms.DateField(
                            label = 'Date Of Birth', 
                            required = False,
                            validators = [validate_date], 
                            widget = forms.SelectDateWidget(
                                years = years,
                                empty_label=("Year", "Month", "Day"),
                                ),
                        )
    
    gender = forms.ChoiceField(
                                label='Gender', 
                                choices=(
                                    ('M', 'Male'),
                                    ('F', 'Female'),
                                    ('O', 'Other'),
                                )
    )

    email = forms.EmailField(
                                label='Email', 
                                widget=forms.TextInput(
                                attrs={'placeholder': 'email@gmail.com'},
                                ),
                            )
    phone_number = forms.CharField(
                                    label='Phone No.', 
                                    validators=[
                                            RegexValidator(regex=r'\d{10}',
                                            message='Enter your 10 digit mobile number.'
                                            )
                                        ],
                                        widget=forms.TextInput(
                                            attrs={'placeholder': '9876543210'},
                                        ),
                                   )
                            
    state = forms.ModelChoiceField(
                                label = 'State',
                                queryset=State.objects.all(),
                                widget=ModelSelect2Widget(
                                    model = State,
                                    search_fields = ['name_icontains'],
                                    dependent_fields={'district': 'districts'},

                                ),
                            )
    district = forms.ModelChoiceField(
                                        label = 'District',
                                        queryset = District.objects.all(),
                                        widget = ModelSelect2Widget(
                                            model = District,
                                            search_fields = ['name_icontains'],
                                            dependent_fields = {'state':'parent_state'},
                                            max_results = 500,
                                        )
                )