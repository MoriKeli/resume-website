from django import forms
from resume.models import Portofolio

class PortofolioForm(forms.ModelForm):
    class Meta:
        model = Portofolio
        fields = ['project_name', 'description', 'category', 'project_thumbnail', 'github_link']
    