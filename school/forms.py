from django import forms
from .models import Student, Staff, Guardian

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date'}),
        }
    
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = '__all__'
        
