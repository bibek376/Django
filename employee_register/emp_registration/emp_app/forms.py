from django import forms
from emp_app.models import Employee

class Employee_Form(forms.ModelForm):

    class Meta:
        model=Employee
        fields=('full_name','emp_code','mobile','position')
        labels={
            'full_name':'Full Name',
            'emp_code':'Employee Code',
            'mobile':'Mobile Number',
            'position':'Designation '
        }
    def __init__(self,*args,**kwargs):
        super(Employee_Form,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="Select"