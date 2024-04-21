from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ShopRegistrationForm,CustomerRegistrationForm,DeliveryBoyRegistrationForm, ShopLoginForm , CustomerLoginForm ,DeliveryBoyLoginForm,ShopEditForm,ProductForm, RentDtlForm
from .forms import CustomerEditForm,DeliveryEditForm,FeedbackForm,AdminLoginForm
from .models import Shop, DeliveryBoy , Customer ,Product,Feedback,Admin
from django.http import HttpResponse
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Cart
from django.http import HttpResponseServerError
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request , 'index.html' )
# views.py
import hashlib

def register_shop(request):
    if request.method == 'POST':
        form = ShopRegistrationForm(request.POST, request.FILES)  # Pass request.FILES for file uploads
        if form.is_valid():
            # Hash the password with MD5
            password = form.cleaned_data['password']
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            # Save the hashed password and form to the database
            shop = form.save(commit=False)
            shop.password = hashed_password
            shop.save()
            return redirect('register_shop')  # Redirect to success page
    else:
        form = ShopRegistrationForm()
    return render(request, 'register_shop.html', {'form': form})

def edit_shop(request):
    # shopid=request.session.get('shop_id')
    # shop = get_object_or_404(Shop, id=shop_id)
    shopid = request.session.get('shop_id')
    shop = Shop.objects.get(id=shopid)
    if request.method == 'POST':
        form = ShopEditForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            # Exclude password from saving
            shop = form.save(commit=False)
            shop.save()
            return redirect('edit_shop', shop_id=shop_id)  # Redirect to success page
    else:
        form = ShopEditForm(instance=shop)
    return render(request, 'edit_shop.html', {'form': form, 'shop': shop})

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            # Hash the password with MD5
            password = form.cleaned_data['password']
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            # Save the hashed password to the database
            form.instance.password = hashed_password
            form.save()
            return redirect('register_customer')  # Redirect to success page
    else:
        form = CustomerRegistrationForm()
    return render(request, 'register_customer.html', {'form': form})

def register_delivery_boy(request):
    if request.method == 'POST':
        form = DeliveryBoyRegistrationForm(request.POST)
        if form.is_valid():
            # Hash the password with MD5
            password = form.cleaned_data['password']
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            # Save the hashed password to the database
            form.instance.password = hashed_password
            form.save()
            return redirect('register_delivery_boy')  # Redirect to success page
    else:
        form = DeliveryBoyRegistrationForm()
    return render(request, 'register_delivery_boy.html', {'form': form})
def edit_delivery(request):
    # shopid=request.session.get('shop_id')
    # shop = get_object_or_404(Shop, id=shop_id)
    deliveryid = request.session.get('deliveryid')
    delivery = DeliveryBoy.objects.get(id=deliveryid)
    if request.method == 'POST':
        form = DeliveryEditForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            # Exclude password from saving
            delivery = form.save(commit=False)
            delivery.save()
            return redirect('edit_delivery', shop_id=shop_id)  # Redirect to success page
    else:
        form = DeliveryEditForm(instance=delivery)
    return render(request, 'edit_delivery.html', {'form': form, 'delivery': delivery})

def customerhome(request):
    
    return render(request , 'customerhome.html' )
    
def deliveryhome(request):
    return render(request , 'deliveryhome.html' )
def shophome(request):
    shop = request.session.get('shop_id')
    print(shop)
    return render(request , 'shophome.html' )


# models.Shop.objects.all().delete()

# # Delete all records from the Customer model
# models.Customer.objects.all().delete()

# # Delete all records from the DeliveryBoy model
# models.
# DeliveryBoy.objects.all().delete()
def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            try:
                admin = Admin.objects.get(email=email, password=hashed_password)
                request.session['admin'] = admin.id  # Store admin id in session
                
                return redirect('admin_home')  # Redirect to admin home page
            except Admin.DoesNotExist:
                form.add_error(None, 'Invalid email or password')
    else:
        form = AdminLoginForm()
    return render(request, 'admin_login.html', {'form': form})



def shop_login(request):
    if request.method == 'POST':
        form = ShopLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            try:
                shop = Shop.objects.get(email=email, password=hashed_password)
                if shop.approvalstatus in [0, 1]:
                    # Approved or Pending, allow login
                    request.session['shop_id'] = shop.id
                    return redirect('shophome')
                elif shop.approvalstatus == 2:
                    # Rejected, do not allow login
                    form.add_error(None, 'Your shop registration has been rejected.')
            except Shop.DoesNotExist:
                form.add_error(None, 'Invalid email or password')
    else:
        form = ShopLoginForm()
    return render(request, 'shoplogin.html', {'form': form})

def customer_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            try:
                customer = Customer.objects.get(email=email, password=hashed_password)
                request.session['customer'] = customer.id
                
                return redirect('customerhome')
            except Customer.DoesNotExist:
                form.add_error(None, 'Invalid email or password')
    else:
        form = CustomerLoginForm()
    return render(request, 'customerlogin.html', {'form': form})

def delivery_boy_login(request):
    if request.method == 'POST':
        form = DeliveryBoyLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            try:
                delivery_boy = DeliveryBoy.objects.get(email=email, password=hashed_password)
                request.session['deliveryid'] = delivery_boy.id
                return redirect('deliveryhome')
            except DeliveryBoy.DoesNotExist:
                form.add_error(None, 'Invalid email or password')
    else:
        form = DeliveryBoyLoginForm()
    return render(request, 'deliveryboylogin.html', {'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.loginid = request.session.get('shop_id')
            
            product.save()
            return redirect('add_product')  # Redirect to a page showing the list of products
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def view_products(request):
    # Check if the shop is logged in
    if 'shop_id' in request.session:
        shop_id = request.session.get('shop_id')
        # Fetch all products belonging to the logged-in shop
        products = Product.objects.filter(loginid=shop_id)
        return render(request, 'view_product.html', {'products': products})
    else:
        # Redirect to login page or handle unauthorized access
        return redirect('login')
def delete_product(request, product_id):
    
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('view_products')  # Redirect to a success page or appropriate URL
    # Handle GET request (optional)
    return render(request, 'confirm_delete_product.html', {'product': product})
 

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, loginid=request.session.get('shop_id'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'add_product.html', {'form': form})


def search_product(request):
    query = request.GET.get('query')
    results = None
    
    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) | Q(category__icontains=query) 
        )
    
    return render(request, 'search_results.html', {'results': results, 'query': query})

def rent_detail(request, id):
    if request.method == 'POST':
        form = RentDtlForm(request.POST)
        if form.is_valid():
            rent_detail = form.save(commit=False)
            rent_detail.loginid = request.session.get('customer')
            rent_detail.productid = id
            
            # Fetch rent amount from Product model
            product = Product.objects.get(id=id)
            rentamt = product.rentamt
            
            # Calculate amount based on days and rentamt
            days = form.cleaned_data['days']
            rent_detail.amount = days * rentamt
            
            rent_detail.save()
            return redirect('search_product')
    else:
        form = RentDtlForm()
    return render(request, 'rent_detail_form.html', {'form': form})


from .forms import PaymentForm
from .models import Bank, Cart, Product
from datetime import date

def payment_form(request, product_id):
    product = Product.objects.get(pk=product_id)
    
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_details = form.cleaned_data
            
            # Check if there is a bank account with the provided details
            try:
                bank_account = Bank.objects.get(
                    cardno=payment_details['cnumber'],
                    cvv=payment_details['cvv'],
                    holdername=payment_details['cowner']
                )
            except Bank.DoesNotExist:
                return render(request, 'paymentform.html', {'form': form, 'error': 'Bank account not found'})
            
            # Payment successful, update payment status
            Cart.objects.create(
                loginid=request.session.get('customer'),
                menuid=product_id,
                currentdate=date.today(),
                quantity=payment_details['quantity'],  # Get quantity from form
                totalamount=product.amount * payment_details['quantity'],
                paymentstatus=1,
                delstatus=0,
                returnstatus=0
            )
            
            print("Payment successful. Redirecting to payment_success.")
            return redirect('search_product')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = PaymentForm()
    
    return render(request, 'paymentform.html', {'form': form})

def edit_customer(request):
    # shopid=request.session.get('shop_id')
    # shop = get_object_or_404(Shop, id=shop_id)
    custid = request.session.get('customer')
    customer = Customer.objects.get(id=custid)
    if request.method == 'POST':
        form = CustomerEditForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            # Exclude password from saving
            customer = form.save(commit=False)
            customer.save()
            return redirect('edit_shop')  # Redirect to success page
    else:
        form = CustomerEditForm(instance=customer)
    return render(request, 'edit_customer.html', {'form': form, 'customer': customer})


def paid_products(request):
    # Retrieve the loginid of the customer
    customer_loginid = request.session.get('customer')

    # Fetch the paid products for the customer where payment status is 1
    paid_products = Cart.objects.filter(loginid=customer_loginid, paymentstatus=1)

    # Fetch the product details for the paid products
    paid_product_details = []
    for cart_item in paid_products:
        product = Product.objects.get(pk=cart_item.menuid)
        paid_product_details.append({
            'cart': cart_item,
            'product': product,
            'quantity': cart_item.quantity,
            'total_amount': cart_item.totalamount,
            'delstatus' : cart_item.delstatus
        })

    return render(request, 'paid_products.html', {'paid_product_details': paid_product_details})



@require_POST
def add_to_cart(request):
    if request.method == 'POST':
        # Get the customer's loginid from the session
        login_id = request.session.get('customer')
        
        # Get the product ID from the form submission
        product_id = request.POST.get('product_id')
        
        # Get the product object based on the product ID
        product = get_object_or_404(Product, id=product_id)
        
        # Define default values for cart item
        quantity = 1  # Default quantity
        total_amount = product.amount  # Assuming product has a price attribute
        
        # Create a cart item
        Cart.objects.create(
            loginid=login_id,
            menuid=product.id,
            currentdate=date.today(),
            quantity=quantity,
            totalamount=total_amount,
            paymentstatus=0,
            delstatus=0,
            returnstatus=0,
        )
        
        # Redirect back to the page where the form was submitted
        return redirect('search_product')  # Change 'search_results' to actual URL name for search results page

    # If the method is not POST, redirect to some page or handle it accordingly
    return redirect('search_product')  # Redirect to some other page if needed

def display_cart(request):
    # Get the logged-in user's loginid from the session
    loginid = request.session.get('customer')
    cart_items = Cart.objects.filter(loginid=loginid, paymentstatus=0)

    # Fetching related product information for each cart item
    cart_with_products = []
    for cart_item in cart_items:
        product = Product.objects.get(id=cart_item.menuid)
        cart_with_products.append({'cart_item': cart_item, 'product': product})

    return render(request, 'cart_view.html', {'cart_with_products': cart_with_products})

def remove_from_cart(request, item_id):
    if request.method == 'POST':
        # Retrieve the cart item to be removed
        cart_item = Cart.objects.get(id=item_id)
        
        # Retrieve product information
        product = cart_item.product
        
        # Perform any additional checks if needed, e.g., ensure the cart item belongs to the logged-in user
        
        # Delete the cart item
        cart_item.delete()
        
        # Fetch updated cart items
        login_id = request.session.get('customer')
        cart_items = Cart.objects.filter(loginid=login_id, paymentstatus=0)
        
        # Pass product and cart items to the template
        return render(request, 'search_results.html', {'product': product, 'cart_items': cart_items})

def logout(request):
    request.session.clear()
    return redirect('index')

def shop_orders(request):
    # Assuming you have already set 'shop_id' in the session
    shop_id = request.session.get('shop_id')

    # Retrieve products belonging to the shop
    products = Product.objects.filter(loginid=shop_id)

    # Retrieve orders for the products belonging to the shop
    orders = Cart.objects.filter(menuid__in=products,paymentstatus=1)

    # Retrieve customer information for each order
    for order in orders:
        customer = Customer.objects.get(id=order.loginid)  # Fetch customer details
        order.customer = customer  # Attach customer information to order

    context = {
        'orders': orders
    }
    return render(request, 'shop_orders.html', context)

def delivery_boys(request,order_id):
    order = get_object_or_404(Cart, id=order_id)
    delivery_boys = DeliveryBoy.objects.all()
    return render(request, 'delivery_boys.html', {'delivery_boys': delivery_boys,'order':order})

from .models import AssignDelBoys

def assign_delivery_boy(request, order_id, delivery_boy_id):
    # Retrieve the order and delivery boy objects
    order = get_object_or_404(Cart, pk=order_id)
    delivery_boy = get_object_or_404(DeliveryBoy, pk=delivery_boy_id)

    # Create an instance of AssignDelBoys and save it
    assignment = AssignDelBoys.objects.create(
        cartid=order_id,
        loginid=delivery_boy.id
    )

    # Redirect back to the Shop Orders page
    return redirect('shop_orders')
def assigned_delivery_boys(request, order_id):
    # Retrieve the AssignDelBoys instance for the given order
    assignment = get_object_or_404(AssignDelBoys, cartid=order_id)

    # Retrieve the assigned delivery boy using the loginid from the assignment
    # delivery_boys = DeliveryBoy.objects.filter( pk=assignment.loginid)
    delivery_boy = get_object_or_404(DeliveryBoy, id=assignment.loginid)

    return render(request, 'assigned_delivery_boys.html', {'delivery_boys': delivery_boy})

def delivery_teams(request):
    
    delivery_boys = DeliveryBoy.objects.all()
    return render(request, 'delivery_teams.html', {'delivery_boys': delivery_boys})

def delivery_orders(request):
    # Retrieve the delivery boy's ID from the session
    delivery_id = request.session.get('deliveryid')

    # Retrieve orders assigned to the delivery boy
    assigned_orders = AssignDelBoys.objects.filter(loginid=delivery_id)

    # Initialize lists to store associated data for each order
    orders_data = []

    # Loop through assigned orders to retrieve associated data
    for assigned_order in assigned_orders:
        # Retrieve Cart, Customer, and Product associated with the current assigned order
        cart = get_object_or_404(Cart, id=assigned_order.cartid)
        customer = get_object_or_404(Customer, id=cart.loginid)
        product = get_object_or_404(Product, id=cart.menuid)

        # Store the associated data in a dictionary
        order_data = {
            'order': assigned_order,  # The assigned order itself
            'cart': cart,
            'customer': customer,
            'product': product,
        }

        # Append the dictionary to the list
        orders_data.append(order_data)

    return render(request, 'delivery_orders.html', {'orders_data': orders_data})

def mark_delivered(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    cart.delstatus = 1  # Set delstatus to 1 to mark as delivered
    cart.save()
    return redirect('delivery_orders')

    
def submit_feedback(request, product_id):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.productid = product_id
            feedback.loginid = request.session.get('customer')
            feedback.save()
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('paid_products')
    else:
        form = FeedbackForm()
    return render(request, 'submit_feedback.html', {'form': form})

def edit_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    if feedback.loginid != request.session.get('customer'):
        # Redirect if the customer is not authorized to edit this feedback
        messages.error(request, 'You are not authorized to edit this feedback.')
        return redirect('paid_products')  # Redirect to home or any other appropriate page
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback updated successfully!')
            return redirect('submit_feedback.html', product_id=feedback.productid)
    else:
        form = FeedbackForm(instance=feedback)
    return render(request, 'submit_feedback.html', {'form': form})

def view_feedback(request):
    customer_login_id = request.session.get('customer')
    feedbacks = Feedback.objects.filter(loginid=customer_login_id)
    feedback_data = []

    # Loop through each feedback instance
    for feedback in feedbacks:
        # Retrieve Product associated with the current feedback
        product = get_object_or_404(Product, id=feedback.productid)

        # Store the associated data in a dictionary
        feedback_dict = {
            'feedback': feedback,  # The feedback itself
            'product': product,
        }

        # Append the dictionary to the list
        feedback_data.append(feedback_dict)
    
    return render(request, 'view_feedback.html', {'feedback_data': feedback_data})

def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    if request.method == 'POST':
        feedback.delete()
        return redirect('view_feedback')  # Redirect to appropriate page after deletion
    # Handle GET requests if necessary

from .models import Complaints
from .forms import ComplaintForm

def enter_complaint(request, product_id):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.productid = product_id
            complaint.loginid = request.session.get('customer')
            complaint.save()
            return redirect('view_complaints')  # Redirect to a success page or any other appropriate page
    else:
        form = ComplaintForm()
    return render(request, 'enter_complaints.html', {'form': form})

def view_complaints(request):
    customer_login_id = request.session.get('customer')
    complaints = Complaints.objects.filter(loginid=customer_login_id)
    complaint_data = []

    # Loop through each feedback instance
    for complaint in complaints:
        # Retrieve Product associated with the current feedback
        product = get_object_or_404(Product, id=complaint.productid)

        # Store the associated data in a dictionary
        complaint_dict = {
            'complaint': complaint,  # The feedback itself
            'product': product,
        }

        # Append the dictionary to the list
        complaint_data.append(complaint_dict)
    
    return render(request, 'view_complaint.html', {'complaint_data': complaint_data})

def edit_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaints, id=complaint_id)
    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('complaint_success')  # Redirect to a success page or any other appropriate page
    else:
        form = ComplaintForm(instance=complaint)
    return render(request, 'enter_complaints.html', {'form': form})

def delete_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaints, id=complaint_id)
    if request.method == 'POST':
        complaint.delete()
        return redirect('view_complaints')

from .forms import ProductReturnForm
from .models import ProductReturn

def product_return(request, cart_id):
    if request.method == 'POST':
        form = ProductReturnForm(request.POST)
        if form.is_valid():
            # Save the form with additional data
            product_return = form.save(commit=False)
            product_return.cartid = cart_id
            product_return.loginid = request.session.get('customer')
            product_return.save()
            return redirect('return_view')  # Redirect to a success URL
    else:
        form = ProductReturnForm()
    return render(request, 'product_return_form.html', {'form': form})

def return_view(request):
    customer_login_id = request.session.get('customer')
    returns = ProductReturn.objects.filter(loginid=customer_login_id)
    return_data = []

    # Loop through each feedback instance
    for ret in returns:
        # Retrieve Product associated with the current feedback
        cart = get_object_or_404(Cart, id=ret.cartid)
        product = get_object_or_404(Product, id=cart.menuid)

        # Store the associated data in a dictionary
        return_dict = {
            'return_det': ret,  # The feedback itself
            'product': product,
        }

        # Append the dictionary to the list
        return_data.append(return_dict)
    
    return render(request, 'return_requests.html', {'return_data': return_data})

def admin_home(request):
    
    return render(request , 'adminhome.html' )

def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shop_detail.html', {'shops': shops})

def approve_shop(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    shop.approvalstatus = 1
    shop.save()
    return redirect('shop_list')

def reject_shop(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    shop.approvalstatus = 2
    shop.save()
    return redirect('shop_list')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def delivery_boy_list(request):
    delivery_boys = DeliveryBoy.objects.all()
    return render(request, 'delivery_boy_list.html', {'delivery_boys': delivery_boys})

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    feedback_data = []

    for feedback in feedbacks:
        product = Product.objects.get(pk=feedback.productid)
        customer = Customer.objects.get(id=feedback.loginid)
        shop = Shop.objects.get(pk=feedback.loginid)

        feedback_data.append({
            'feedback': feedback.feedback,
            'product_name': product.name,
            'shop_name': shop.name,
            'customer_name': customer.customername,
            'date': feedback.currentdate,
        })

    return render(request, 'feedback_list.html', {'feedback_data': feedback_data})

def complaint_list(request):
    complaints = Complaints.objects.all()
    complaint_data = []

    for complaint in complaints:
        product = Product.objects.get(pk=complaint.productid)
        customer = Customer.objects.get(pk=complaint.loginid)

        complaint_data.append({
            'complaint': complaint.complaint,
            'product_name': product.name,
            'customer_name': customer.customername,
            'date': complaint.currentdate,
            'ad_reply': complaint.adreply,
        })

    return render(request, 'complaint_list.html', {'complaint_data': complaint_data})

