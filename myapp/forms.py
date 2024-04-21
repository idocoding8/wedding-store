# forms.py
from django import forms
from .models import Shop, Customer, DeliveryBoy ,Login ,Product,ProductReturn

class ShopRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    DISTRICT_CHOICES = [
        ('Alappuzha', 'Alappuzha'),
        ('Ernakulam', 'Ernakulam'),
        ('Idukki', 'Idukki'),
        ('Kannur', 'Kannur'),
        ('Kasaragod', 'Kasaragod'),
        ('Kollam', 'Kollam'),
        ('Kottayam', 'Kottayam'),
        ('Kozhikode', 'Kozhikode'),
        ('Malappuram', 'Malappuram'),
        ('Palakkad', 'Palakkad'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Thiruvananthapuram', 'Thiruvananthapuram'),
        ('Thrissur', 'Thrissur'),
        ('Wayanad', 'Wayanad'),
    ]

    dist = forms.ChoiceField(choices=DISTRICT_CHOICES)
    address = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Shop
        fields = ['name', 'image', 'address', 'pincode', 'dist', 'city', 'contact','email', 'password']

class ShopEditForm(forms.ModelForm):
   

    DISTRICT_CHOICES = [
        ('Alappuzha', 'Alappuzha'),
        ('Ernakulam', 'Ernakulam'),
        ('Idukki', 'Idukki'),
        ('Kannur', 'Kannur'),
        ('Kasaragod', 'Kasaragod'),
        ('Kollam', 'Kollam'),
        ('Kottayam', 'Kottayam'),
        ('Kozhikode', 'Kozhikode'),
        ('Malappuram', 'Malappuram'),
        ('Palakkad', 'Palakkad'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Thiruvananthapuram', 'Thiruvananthapuram'),
        ('Thrissur', 'Thrissur'),
        ('Wayanad', 'Wayanad'),
    ]

    dist = forms.ChoiceField(choices=DISTRICT_CHOICES)
    address = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Shop
        fields = ['name', 'image', 'address', 'pincode', 'dist', 'city', 'contact','email']

class CustomerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Customer
        fields = ['customername', 'address', 'contact', 'email', 'password']

class DeliveryBoyRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    DISTRICT_CHOICES = [
        ('Alappuzha', 'Alappuzha'),
        ('Ernakulam', 'Ernakulam'),
        ('Idukki', 'Idukki'),
        ('Kannur', 'Kannur'),
        ('Kasaragod', 'Kasaragod'),
        ('Kollam', 'Kollam'),
        ('Kottayam', 'Kottayam'),
        ('Kozhikode', 'Kozhikode'),
        ('Malappuram', 'Malappuram'),
        ('Palakkad', 'Palakkad'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Thiruvananthapuram', 'Thiruvananthapuram'),
        ('Thrissur', 'Thrissur'),
        ('Wayanad', 'Wayanad'),
    ]

    district = forms.ChoiceField(choices=DISTRICT_CHOICES)

    class Meta:
        model = DeliveryBoy
        fields = ['delname', 'address', 'pincode', 'district', 'city', 'contactno', 'email', 'password']
class DeliveryEditForm(forms.ModelForm):
    DISTRICT_CHOICES = [
        ('Alappuzha', 'Alappuzha'),
        ('Ernakulam', 'Ernakulam'),
        ('Idukki', 'Idukki'),
        ('Kannur', 'Kannur'),
        ('Kasaragod', 'Kasaragod'),
        ('Kollam', 'Kollam'),
        ('Kottayam', 'Kottayam'),
        ('Kozhikode', 'Kozhikode'),
        ('Malappuram', 'Malappuram'),
        ('Palakkad', 'Palakkad'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Thiruvananthapuram', 'Thiruvananthapuram'),
        ('Thrissur', 'Thrissur'),
        ('Wayanad', 'Wayanad'),
    ]

    district = forms.ChoiceField(choices=DISTRICT_CHOICES)

    class Meta:
        model = DeliveryBoy
        fields = ['delname', 'address', 'pincode', 'district', 'city', 'contactno', 'email']

class ShopLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomerLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class DeliveryBoyLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class ProductForm(forms.ModelForm):
    SELLING_CHOICES = (
        ('sell', 'Sell'),
        ('rent', 'Rent'),
        ('both', 'Both'),
    )
    CATEGORY_CHOICES = (
        ('kids', 'Kids'),
        ('women', 'Women'),
        ('men', 'Men'),
    )
    selling = forms.ChoiceField(choices=SELLING_CHOICES, widget=forms.Select)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select)
    details = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Product
        fields = ['category', 'name', 'image', 'details', 'rentamt', 'amount', 'selling']

from .models import RentDtl

class RentDtlForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = RentDtl
        fields = ['days', 'address', 'quantity']

class PaymentForm(forms.Form):
    cnumber = forms.CharField(label='Card Number', max_length=16)
    edate = forms.CharField(label='Expiration Date', max_length=70)
    cvv = forms.CharField(label='CV Code', max_length=3)
    cowner = forms.CharField(label='Card Owner', max_length=100)
    quantity = forms.IntegerField(label='Quantity')
    
class CustomerEditForm(forms.ModelForm):
    
    address = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Customer
        fields = ['customername', 'address', 'contact', 'email']
        

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    feedback = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Feedback
        fields = ['feedback']

from .models import Complaints

class ComplaintForm(forms.ModelForm):
    complaint = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Complaints
        
        fields = ['complaint']
        
class ProductReturnForm(forms.ModelForm):
    reason = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = ProductReturn
        fields = ['reason']

    def __init__(self, *args, **kwargs):
        super(ProductReturnForm, self).__init__(*args, **kwargs)
        
class AdminLoginForm(forms.Form):
    email = forms.EmailField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
