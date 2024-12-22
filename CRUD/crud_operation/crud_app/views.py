from django.shortcuts import render,redirect,get_object_or_404
from crud_app.models import Info_Model

# Create your views here.

def home(request):
    return render(request,'crud_app/templates/home.html')


def success_view(request):
    return render(request,'crud_app/templates/success.html')

def create_view(request):
    if request.method=='POST':
        v_title=request.POST.get('title')
        v_desc=request.POST.get('description')

        save_to_db=Info_Model.objects.create(title=v_title,description=v_desc)
        save_to_db.save()
        
        return redirect('success_page')

    return render(request,'crud_app/templates/basic_form.html')


def to_list_all(request):
    data=Info_Model.objects.all()

    return render(request,'crud_app/templates/all_data.html',{'datas':data})


def detailed_data(request,pk):
    data=Info_Model.objects.get(id=pk)

    return render(request,'crud_app/templates/single_data.html',{'data':data})



def book_edit(request, id):
    book = get_object_or_404(Info_Model, id=pk)

    if request.method == 'POST':
        # Process the form data manually
        title = request.POST.get('title')
        description = request.POST.get('description')
        # Add more fields as needed

        # Update the book instance with the form data
        book.title = title
        book.author = author
        # Update more fields as needed

        book.save()

        return redirect('book_detail', pk=book.pk)
    else:
        # Pre-fill the form with existing data
        form_data = {
            'title': book.title,
            'author': book.author,
            # Add more fields as needed
        }

    return render(request, 'library/book_form.html', {'form_data': form_data})