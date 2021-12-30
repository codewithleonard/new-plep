from django import forms

class ClientForm(forms.Form):
    PROJECT_CATG = (
        ('Web Project', 'Web Project'),
        ('Mobile App Dev Project', 'Mobile App Dev Project'),
        ('Machine Learning Project', 'Machine Learning Project'),
        ('Project', 'Project'),
        ('Others', 'Others'),
    )
    MODE = (
        ('Individual', 'Individual'),
        ('Group', 'Group'),
    )
    fullname = forms.CharField(max_length=200, label="Fullname")
    supervisor_name = forms.CharField(max_length=200, label="Supervisor Name")
    project_catg = forms.CharField(max_length=200, label="Project Category", widget=forms.Select(choices=PROJECT_CATG))
    others = forms.CharField(label="Specify", required=True)
    project_name = forms.CharField(max_length=200, label="Project Name")
    project_description = forms.CharField(widget=forms.Textarea)
    program_lang = forms.CharField(label="Programming Language to Use (Optional)", required=False)
    email = forms.EmailField(label="Valid Email")
    phone = forms.CharField(max_length=20, label="Phone Number")
    project_mode = forms.ChoiceField(widget=forms.RadioSelect, choices=MODE, label="Mode of Project")
    no_of_member = forms.IntegerField(label="How many are you in the group?", required=True)
