from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"



MOOD_CHOICES= [
    ('Happie', 'Happie'),
    ('Angrie', 'Angrie'),
    ('Dehydratie', 'Dehydratie'),
    ('Depressie', 'Depressie'),
    ('Excitie', 'Excitie'),
    ('Unwellie', 'Unwellie'),
    ]
RESTAURANT_CHOICES=[
   ('PizzaHut','PizzaHut'),
]
FOOD_CHOICES=[
('Pasta','Pasta'),
]
class Feedback(forms.Form):

    Restaurant=forms.CharField(widget=forms.Select(choices=RESTAURANT_CHOICES))
    Food=forms.CharField(widget=forms.Select(choices=FOOD_CHOICES))
    Mood= forms.CharField(label='How are you feeling today?', widget=forms.Select(choices=MOOD_CHOICES))
    Rating=forms.DecimalField(label='Rating(On a scale of 5)', max_value=5, min_value=0)
