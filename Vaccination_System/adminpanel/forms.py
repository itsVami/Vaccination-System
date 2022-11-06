from django import forms
from .models import Admin
from patient.models import Patient
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

class ProfileForm(forms.ModelForm):
    def __init__(self , *args , **kwargs):
        user = kwargs.pop('user')

        super(ProfileForm , self).__init__(*args , **kwargs)

        self.fields['username'].help_text = None
        
        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True
            self.fields['special_user'].disabled = True
            self.fields['is_author'].disabled = True
        

    class Meta:
        model = Admin
        fields = [
            'username' , 'email' , 'first_name' , 'last_name' , 'special_user' , 'is_author' , 'profile_avatar'
        ]



class PatientForm(forms.ModelForm):
    def __init__(self , *args , **kwargs):
        super(PatientForm , self).__init__(*args , **kwargs)

        self.fields["birth_date"]=JalaliDateField(label=('تاریخ تولد'),widget=AdminJalaliDateWidget)


    class Meta:
        model = Patient
        fields = '__all__'