from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Role, Employee
# Create your views here.
def index(request):
    context = {}
    context['title'] = "Home"
    """ -------------   Show Employees Data    ----------- """
    context['employee'] = Employee.objects.all()
    return render(request, 'index.html', context)
def add_employee(request):
    context = {}
    context['title'] = "Add"
    context['role'] = Role.objects.all()
    context['department'] = Department.objects.all()
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        department = int(request.POST['department'])
        role = int(request.POST['role'])
        employee = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, department_id=department, role_id=role)
        if employee:
            msg = "ok"
            employee.save()
            context["login_msg"] = msg
        else:
            msg = "no"
            context["login_msg"] = msg



    return render(request, 'add.html', context)
def remove_employee(request, id = 0):
    context = {}
    context['title'] = "Remove"
    """ -------------   Show Employees Data    ----------- """
    context['employee'] = Employee.objects.all()
    if id:
        try:
            remove_msg = "ok"
            remove = Employee.objects.get(id=id)
            remove.delete()
            context['remove_msg'] = remove_msg
        except:
            remove_msg = "no"
            context['remove_msg'] = remove_msg
    return render(request, 'index.html', context)
def edit_employee(request, id):
    context = {}
    context['title'] = "Update"
    context['data'] = Employee.objects.get(id=id)
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        n_id = request.POST['id']
        emp = Employee.objects.filter(id=n_id).update(first_name=fname, last_name=lname,salary=salary,bonus=bonus,phone=phone)
        if emp:
            update_msg = "ok"
            context["update_msg"] = update_msg
        else:
            update_msg = "no"
            context["update_msg"] = update_msg



    return render(request, 'change.html', context)