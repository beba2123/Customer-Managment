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