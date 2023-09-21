# database queries
lelts say there is  a customer, product and also order table inside our models file.
# -->(1) Returns all customers from the customer table.
customer = Customer.objects.all() -> and if we want to return the first or the second we write Customer.objects.first(); or second() in a place of first();

# --> (2) returns single customer in table by name or by id or 
customer = Customer.objects.get(id='id No' or name = 'name of the table', or email='email name')

# --> return all information related to that customer name
firstCustomer = Customer.objects.get(id=1);
lets says on id = 1 the customer name is Abebe so indorder to have all orders or information related to abebe..-> orders = firstCustomer.order_set.all() 

# --> for returning the first person that order
firstOrder = Order.objects.first()
name = firstOrder.customer.name
print(name) ==> abebe


# --> for knowing that how the total count for each product ordered 
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
         allOrders[orders.product.name] += 1
    else:
         allOrders[order.product.name] = 1

allOrders = {'banana' : 2, 'Guns': 1};

# for returning how much times the 'Ball' is ordered by the firstCustomer is
ballOrders = firstCustomer.order_set.filter(product__name = 'Guns').count()
# the meaning of " __ " double underscore in queries is for telling the relation between class name like the order has manytomany relation ship with products so that is for reason.
print(ballOrders) --> 2 



# Template tags

-->> in template tags we use two thing {{}} used for passing data for the temlate and {% %} used for writing url or writing loop function inside it.


# Form in django and Crud application


# 1 create order
-> first we have to import modelform from django.forms then import one of  the model that you want to fill out like Order or Customer..or something else.
     class OrderForm(ModelForm):
          class Meta:
               model = Order
               fields = ['__all__']  this holds all the table inside the order class.
-> then we have to come back to views.py and import OrderForm from form.py file and then 
     def createOrder(request):
          form = OrderForm(): first we store a order form inside the form
               if request.method == 'POST': then check it if it is post method
                    form = OrderForm(request.POST)    contains all the submitted form. (request.post method is like  dictionary form that store all sumbitted information inside the form)
                    if form.is_valid(): //then check it if it valid 
                         form.save() // save it 
                         return redirect('home')  //lastly redirect it to home page.
     
#  2 update order
     def update_order(request, pk): -> first create a function that is used for update an order.
          order = Order.objects.get(id=pk) #-> then find one of the row inside a table using it id
          form = OrderForm(instance=order) #the instance of the order table before we update it the previous information that we submited it.
          
          if request.method == 'POST':
               form = OrderForm(request.POST, instance=order)
               if form.is_valid():
               form.save()
               return redirect('/')
          context = {'form': form}
          return render(request, 'acounts/create_form.html', context)

# delete order
          
          def delete_order(request, pk):
               order = Order.objects.get(id=pk) #-> find the table based on its id
               if request.method == 'POST': #if we say confirm
                    order.delete() #the order is going to be deleted 
                    return redirect('/') # then we will be redirect to the home page 
               context={'item':order}

               return render(request, 'acounts/delete_order.html', context)

# Filter in django

-> first install filter using pip install django-filter
-> then we create a file called  filters.py inside our app folder
     1st we have to import django_filter and import the models
     class OrdersFilter(django_filters.FilterSet):
          class Meta:
               model = Order -> write filter class 
               fields = '__all__' -> all the rows inside the orders table.
-> there are other things that we can do inside our filter file like excluding one of the row and we can import diffrent package from the django filter like 
     DateFilter, CharFilter
               Eg start_date = DateFilter(field_name='date_created', lookup_expr='gte')

               end_date = DateFilter(field_name='date_created', lookup_expr='lte')
               note = CharFilter(field_name='note', lookup_expr='icontains')
               
-> then we goes to our view file and lets say that we are going to filter on a customer page so we goes to customer  function
     -> from .filters import OrdersFilter ->import the class from filter
     myfilter = OrderFilter(request.GET, queryset='the model that we want')

# create registration and login page 

-> we can use diffrent method to create a login and registration page so in these project i used UserCreationForm that is imported from django so this form has username, email ,password and other form which is default form in django.

-> so first i create forms.py file then import user creation form then create a class and make a form page using it.
->   class CreateUserForm(UserCreationForm): 
               class Meta:
                    model = User
                    fields = ['username', 'email', 'password1', 'password2']

-> then import the CreateUserForm to a views.py then under registerpage function

def registerpage(request):
     form = CreateUserForm() ==> storing inside the form
     
     request.method == POST:
          form = CreateUserForm(request.POST)
          if form.is_valid():
               form.save()
               user = form.cleaned_data['username'] -> accessing user data clean data from the validated submit form.
               messages.successs(request, user + ' created account successfully ')
               return redirect('/')


# login page
-> first import the authentication and login page from django.contrib.auth 
def loginPage(request):

     if request.method == 'POST':
          username= request.POST['username'] #got the submitted username
          password = <PASSWORD>.POST['<PASSWORD>'] # got the submitted password
          user = authenticate(request, username=username, password=<PASSWORD>) # authenticate it
          if user is not None :    if the authenticate user is right 
               login(request, user)     # login the user
               messages.success(request,'You are logged in succefully!') # give succesfull message
               return redirect('home/')
          else:
               message.error(request, 'invalid credential..!!')
     
     return render(request , 'login/login.html' )


# create one to one relationship with the built in user model..

-> first in our model file we import the user model from django.contrib.auth import User the in one of our class we related the User with one to one relation with it.

     user = model.OneToOneField(User, delete=models.CASCADE, null=TRUE)  # using this method..

=> then after in the views.py file we are  going to write when user is register
-> it is going to create in the customer class.
     Customer.objects.create(user=user)


# Signaling

=> it is a mechanism for allowing certain senders to notify a set of recievers that some of the action has taken place.they are used to decoupled applications to get notified when certain actions occur elsewhere in the application.

signals are used for sending notifications or events to other apps.
=> so here is the first step that i  used in my project 
1st i just import pre_save from django.db.models.signals
then in this project i used the  signal for notify when a new customeer is registered in the website
 



  