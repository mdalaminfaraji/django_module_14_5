from django import forms
import datetime
from .models import GeeksModel 
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class contactForm(forms.Form):
    name = forms.CharField( initial="Your Name")
    email = forms.EmailField(label = "User Email")
    comment= forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree=forms.BooleanField(initial=True)
    date=forms.DateField( initial=datetime.date.today, required=False)
    birth_year=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value=forms.DecimalField()
    message=forms.CharField(max_length=10)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    choice_color=forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    multipleChoice=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple ,choices=FAVORITE_COLORS_CHOICES)
    
    

class InputForm(forms.Form): 
	
	first_name = forms.CharField(max_length = 200) 
	last_name = forms.CharField(max_length = 200) 
	roll_number = forms.IntegerField( 
					help_text = "Enter 6 digit roll number"
					) 
	password = forms.CharField(widget = forms.PasswordInput()) 
 
class GeeksForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = GeeksModel 
        fields = "__all__"

    
    
    