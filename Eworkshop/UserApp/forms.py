from .models import insurance
from django.forms import ModelForm

class insuranceform(ModelForm):
    class Meta:
        model=insurance
        fields=['owner','vehicle_no','vehicle_type','house_name','place','issue_date','expiry_date']
