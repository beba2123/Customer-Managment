from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters  import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form  = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data['username']
                messages.success(request, user + ' created account successfully ')
                return  redirect('login')
            else:
                form = CreateUserForm() #the request is not POST method the user is presented with blank

        context = {'form': form}
        return render(request, 'acounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username= request.POST['username']
            password = request.POST['password']
            user  = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You successful logged in')
                return redirect('home')
            else:
                messages.error(request,'Invalid Credentials!')
        context={}
        return render(request, 'acounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    order_delieverd = orders.filter(status = 'Delivered').count()
    order_pending = orders.filter(status = 'Pending').count()
    context = {'orders': orders, 'customers': customers,'order_delivered': order_delieverd, 'order_pending': order_pending, 'total_orders': total_orders}
    return render(request, 'acounts/dashboard.html', context)

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return  render(request,'acounts/products.html', {'products': products})
@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs

    context = {'customer': customer, 'orders': orders, 'orders_count':orders_count, 'myfilter':myfilter}
    return render(request, 'acounts/customer.html', context)

@login_required(login_url='login')
def create_order(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=("product", "status"), extra=5)
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial={'customer':customer}) before we create inline form sets
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        # print('printing post', request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
        

    context={'formset':formset}
    return render(request, 'acounts/create_form.html', context)

@login_required(login_url='login')
def update_order(request, pk):
    
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order) #the instance of the order table before we update it the previous information that we submited it.
    
    if request.method == 'POST':
     form = OrderForm(request.POST, instance=order)
     if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'acounts/create_form.html', context)

@login_required(login_url='login')
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST': #if we say confirm
        order.delete() #the order is going to be deleted 
        return redirect('/') # then we will be redirect to the home page 
    context={'item':order}

    return render(request, 'acounts/delete_order.html', context)





# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .models import *
# from classes.models import *
# from teachers.models import *
# from accounts.decorators import student_required
# # Create your views here.
# @student_required
# def student_dashboard(request, pk):
#     user = request.user     #to retriev the data based on the logged in user
#     students = Student.objects.filter(user=user) #filtering students based on the it's user

#     if students.exists():
#         student = students.first() #if it exists take the first one from the queryset
#         courses = Subject.objects.all().order_by('-id')  #retrieving all subjects and ordering them by id descending
#         stu_class = Class_room.objects.get(id=pk)
    
#         context={
#         'student':student,
#         "classes":stu_class,
#         "courses": courses
#         }

#         # get class schedule for each class
#         class_schedule = {}
#         for class_obj in stu_class: ##iterate for each classes
#             schedule = classSchedule.objects.filter(class_info= class_obj) #classSchedule is not in the model..
#             class_schedule[class_obj] = schedule

#         context['class_schedules'] = class_schedule #adding class schedule to the context becouse it is dictionary we cannot write it in dictionar we just store it directly.
#         return render (request,'students/student-dashbord.html',context )
#     else:
#         messages.error("You are not a registered student")
#         return redirect('home')
    

# @student_required
# def view_grades(request):
#     try:
#         students = Student.objects.get(Student, user=request.user) #like assuming that the user model is associated  with the student 
#     except Student.DoesNotExist:
#         return render(request, 'dashboard/student_not_found.html')
    
#     grades = Grade.objects.filter(students=students)  #add Grade class it is not added.

#     # i want to add this one but there is no table related to it
#     test_results = TestResult.objects.filter(students=students)
#     assignment_results = AssignmentResult.objects.filter(students=students)
#     final_test_results = FinalTestResult.objects.filter(students=students)

#     context = {
#         'test_results': test_results,
#         'assignment_results': assignment_results,
#         'final_test_results': final_test_results,
#         'grades' : grades,
#         'students':students
#     }
#     return render(request,"students/view_grades.html",context)


# def view_attendance(request):
#     student = Student.objects.get(user = request.user)
#     Attendance_record = Attendance.objects.filter(student=student)

#     context = {'student': student,
#                 'attendance_record': Attendance_record
#             }
#     return render(request,  'dashboard/view_attendance.html', context)

# def view_resources(request):
#     student = get_object_or_404(Student, user=request.user)
#     enrolled_classes = student.class_room_id.all()

#     teacher_resource_mapping  = {}

#     for enrolled_class in enrolled_classes:
#         teacher = enrolled_class.teacher
#         resources = Resource.objects.filter(uploaded_by = teacher)
#         teacher_resource_mapping[teacher] = resources
#         context={
#             "enrolled": True if (enrolled_class == Class_room.objects.get(pk=1)) else False ,
#             "teacher" : teacher,
#             "resources" : resources
#             }
#         return render(request,'dashboard/view_resources.html',context )