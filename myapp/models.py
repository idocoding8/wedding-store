from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator,ValidationError
def validate_no_numbers(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('Name should not contain numbers.')
class Shop(models.Model):
    name = models.CharField(max_length=20, validators=[MaxLengthValidator(20)])
    image = models.FileField(upload_to='images/',max_length=250,null=True,default=None)
    address = models.CharField(max_length=60, validators=[MaxLengthValidator(60)])
    pincode = models.CharField(max_length=6, validators=[RegexValidator(regex='^[0-9]{6}$', message='Please enter a valid 6-digit pincode.')])
    dist = models.CharField(max_length=20, validators=[MaxLengthValidator(20)])
    city = models.CharField(max_length=20, validators=[MaxLengthValidator(20)])
    contact = models.CharField(max_length=12, validators=[RegexValidator(regex='^[0-9]{10,12}$', message='Please enter a valid 10 to 12-digit contact number.')])
    email = models.EmailField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    approvalstatus = models.IntegerField(choices=((0, 'Pending'), (1, 'Approved'), (2, 'Rejected')), default=0)

class Customer(models.Model):
    customername = models.CharField(max_length=20, validators=[MaxLengthValidator(20), validate_no_numbers])
    address = models.CharField(max_length=60, validators=[MaxLengthValidator(60)])
    contact = models.CharField(max_length=12, validators=[RegexValidator(regex='^[0-9]{10,12}$', message='Please enter a valid 10 to 12-digit contact number.')])
    email = models.EmailField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    
    
    
class DeliveryBoy(models.Model):
    delname = models.CharField(max_length=20, validators=[MaxLengthValidator(20)])
    address = models.CharField(max_length=60, validators=[MaxLengthValidator(60)])
    pincode = models.CharField(max_length=6, validators=[RegexValidator(regex='^[0-9]{6}$', message='Please enter a valid 6-digit pincode.')])
    district = models.CharField(max_length=20, validators=[MaxLengthValidator(20)])
    city = models.CharField(max_length=20, validators=[MaxLengthValidator(20)])
    contactno = models.CharField(max_length=12, validators=[RegexValidator(regex='^[0-9]{10,12}$', message='Please enter a valid 10 to 12-digit contact number.')])
    email = models.EmailField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
 

class AssignDelBoys(models.Model):
    cartid = models.CharField(max_length=11)
    loginid = models.IntegerField()
    currentdate = models.DateField(auto_now_add=True)

class Bank(models.Model):
    accountno = models.CharField(max_length=15)
    holdername = models.CharField(max_length=20)
    bankname = models.CharField(max_length=20)
    branchname = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=11)
    cardno = models.CharField(max_length=12)
    cvv = models.IntegerField()
    edate = models.DateField()
    tamount = models.CharField(max_length=7)
    contactno = models.CharField(max_length=12)

class Cart(models.Model):
    loginid = models.IntegerField()
    menuid = models.IntegerField()
    currentdate = models.DateField()
    quantity = models.IntegerField()
    totalamount = models.IntegerField()
    paymentstatus = models.IntegerField()
    delstatus = models.IntegerField()
    returnstatus = models.IntegerField()

class Complaints(models.Model):
    complaint = models.CharField(max_length=60, validators=[MaxLengthValidator(60)])
    productid = models.PositiveIntegerField()
    loginid = models.PositiveIntegerField()
    currentdate = models.DateField(auto_now_add=True)
    adreply = models.CharField(max_length=60, validators=[MaxLengthValidator(60)])

class Feedback(models.Model):
    feedback = models.CharField(max_length=60, validators=[MaxLengthValidator(60)])
    productid = models.PositiveIntegerField()
    loginid = models.PositiveIntegerField()
    currentdate = models.DateField(auto_now_add=True)

class Login(models.Model):

    email = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
   

class Offers(models.Model):

    productid = models.IntegerField()
    offers = models.CharField(max_length=60, validators=[MaxLengthValidator(60)])
    loginid = models.IntegerField()
    currentdate = models.DateField()
    offerlimit = models.IntegerField()

class Payment(models.Model):
    cowner = models.CharField(max_length=20)
    card = models.IntegerField()
    cvv = models.IntegerField()
    edate = models.DateField()
    loginid = models.IntegerField()
    cdate = models.DateField()
    amount = models.IntegerField()

class Product(models.Model):
    category = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='images/',max_length=250,null=True,default=None)
    details = models.CharField(max_length=60)
    rentamt = models.IntegerField()
    amount = models.IntegerField()
    loginid = models.IntegerField()
    selling = models.CharField(max_length=10)

class ProductReturn(models.Model):
    reason = models.CharField(max_length=60)
    cartid = models.IntegerField()
    loginid = models.IntegerField()
    date = models.DateField(auto_now_add=True)

class RentDtl(models.Model):
    days = models.IntegerField()
    address = models.CharField(max_length=60)
    quantity = models.IntegerField()
    productid = models.IntegerField()
    currentdate = models.DateField(auto_now_add=True)
    loginid = models.IntegerField()
    amount = models.IntegerField()

class Admin(models.Model):
    email=models.EmailField(max_length=32)
    password=models.CharField(max_length=32)
    
