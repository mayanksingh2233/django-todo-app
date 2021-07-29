from django.shortcuts import redirect, render
from .models import Todo, contact

# Create your views here.
def home(request):
    context={
        "page":"Home context",
        "logged":True 
    }
    return render(request,'home.html',context)

def Contact(request):
    contact_obj = contact.objects.all()
    print(contact_obj)
    context={
        "page":"contact context",
        "logged":False,
        "contacts":contact_obj }
    return render(request,'contact.html',context)

def about(request):
    context={
        "page":"about context",
        "logged":False
    }
    return render(request,'about.html',context)

def todo(request):
    if request.method =="POST":
        todo =request.POST['todo']
        if todo is not None:
            todo_obj=Todo(todo_name=todo)
            todo_obj.save()
        return redirect('/todo')
    todo_object=Todo.objects.all()
    context={
        "todo_obb":todo_object
    }
    return render(request,'todo.html',context)

def delete_as_complete(request,id):
    try:
        todo=Todo.objects.get(id=id)
        todo.delete()
    except Todo.DoesNotExist:
        pass
    return redirect("/todo")
def mark_as_complete(request,id):
    try:
        todo=Todo.objects.get(id=id)
        todo.is_complete =True
        todo.save()
    except Todo.DoesNotExist:
        pass
    return redirect("/todo")
