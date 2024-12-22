from django.shortcuts import render,redirect,get_object_or_404
from emp_app.forms import Employee_Form
from emp_app.models import Employee
# Create your views here.


def emp_list(request):
    employee_details=Employee.objects.all()
    context={
        'employees':
        employee_details
    }
    return render(request,'emp_app/templates/employee_list.html',context)


def emp_update_insert(request):
    if request.method=='POST':
        form=Employee_Form(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully.")
        else:
            print("Form is not valid:", form.errors)
        return redirect('emp_list')
    else:
        form=Employee_Form()
        return render(request,'emp_app/templates/employee_form.html',{'form':form})

 
def emp_delete(request,pk):
    v_form=get_object_or_404(Employee,id=pk)

    if request.method=='POST':
        v_form.delete()
        return redirect('emp_list')
    
    return render(request, 'emp_app/templates/emp_del_con.html', {'forms': v_form})

def edit_employee(request,pk):
    v_form=get_object_or_404(Employee,pk=pk)

    if request.method=='POST':
        form=Employee_Form(request.POST or None,instance=v_form)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form=Employee_Form(instance=v_form)

    return render(request,'emp_app/templates/employee_form.html',{'form':form})
  
