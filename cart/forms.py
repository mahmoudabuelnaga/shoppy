from django import forms

PRODUCT_QUENTITY_CHOICES = [(i, str(i)) for i in range(1,21)]

class CartAddProdcutForm(forms.Form):
    quentity = forms.TypedChoiceField( 
                    widget=forms.Select(attrs={
                        'style':"width: 100px",
                        'class':"form-control",
                        'aria-label':"Search",
                        'value':"1",
                        'type':"number",
                    }),
                    choices=PRODUCT_QUENTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)