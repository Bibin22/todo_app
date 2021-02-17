from django import forms

class TaskCreateForms(forms.Form):
    task_name = forms.CharField(max_length=120)
    date = forms.CharField(max_length=60)
    status = forms.CharField(max_length=60)


class TaskSearchForms(forms.Form):
    date = forms.CharField(max_length=60)


class TaskUpdateForm(forms.Form):
    task_name = forms.CharField(max_length=120)
    date = forms.CharField(max_length=60)
    status = forms.CharField(max_length=60)