from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['id', 'fullname', 'empcode', 'mobile', 'position']
        labels = {
            'fullname': 'Full Name',
            'empcode': 'Emp Code',

        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

    #     self.fields['position'].empty_label ="Select"

    def save(self, commit=True):
        instance = super(EmployeeForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance


class employeeSearchForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['empcode']
