from django.shortcuts import render, redirect
from .forms import EmployeeForm, employeeSearchForm
from .models import Employee
from django_filters import filters


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm(request.GET)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employeedetails/form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        return redirect("/employee/list")


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect("/employee/list")


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employeedetails/list.html', context)


def employee_search(request):
    form = employeeSearchForm(request.POST or None)
    context = {"form": form}
    if request.method == 'POST':
        form = employeeSearchForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data
            queryset = Employee.objects.filter(empcode__contains=x['empcode'])
            context = {
                "queryset": queryset,
                "form": form,
            }
    return render(request, 'employeedetails/search.html', context)
