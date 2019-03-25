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
        Date validation for DOB and age above 18 years
    """
    if datetime.date.today() < date:
        raise ValidationError(_('Date of birth can\'t be a future date'))
    if datetime.date.today().year - date.year < 17:
        raise ValidationError(_('You must be atleast 18 years old.')) 
class MemberRegistrationForm(forms.Form):
    """
        Form for registration of members.
    """
    name = forms.CharField(label='Name',
                           validators=[
                               RegexValidator(
                                        regex=r'([A-Za-z]|\s)+',
                                        message='Invalid Characters in name',
                                        )
                                 ],
                           )

    dob = forms.DateField(
                            label = 'Date Of Birth', 
                            required = False, 
                            validators=[validate_date],
                            widget=forms.widgets.DateInput(attrs={'type': 'date'})
                                
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
                                required = False,
                            )
    phone_number = forms.CharField(
                                    label='Phone No.', 
                                    validators=[
                                            RegexValidator(regex=r'\d{10}',
                                            message='Enter your 10 digit mobile number.'
                                            )
                                        ],
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
    address = forms.CharField(
                label = 'Address',
                required = False,
                max_length = 200,
                widget=forms.Textarea,
            )
    pin_code = forms.CharField(
                    label = 'Pin Code',
                    required = False,
                    validators=[
                        RegexValidator(
                            regex=r'\d{6}',
                            message = 'Enter a valid pin code',
                        )
                    ]
                )
    voterId = forms.CharField(
                    label = 'Voter ID',
                    required = False,
                    validators=[
                                RegexValidator(
                                                regex=r'[A-Z]{3}\d{7}',
                                                message='Enter valid VOTER ID number.',
                                        )
                                ],
                )
    disclaimer = '''I am above 18 years , and not enrolled as a government employee.
                    I am not a member of any other political party registered with the Election Commission of India.
                    I am not a member with any organization whose views, policies or actions are in 
                    conflict with the objective of the party. I have not been convicted of any offense 
                    involving moral turpitude. I hereby consent to receiving any communication from the party either in writing, 
                    electronically and/or in any audio-visual format via phone (including SMS/MMS), email and/or at my address.'''
    Iagree = forms.BooleanField(
                label= disclaimer,
            )