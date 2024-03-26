from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

#bosh sahifani belgilash
def hometodo(request):
    todos=Todo.objects.filter(user=request.user)
    form=TodoForm()
    if request.method=="POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.user=request.user
            todo.save()
            return redirect('todohome')


    context={
        "todos":todos,
        "form":form
    }
    return render(request,"home.html",context)


#todoni o'chirish
def delete_todo(request,pk=None):
    todo=Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todohome')


#todo checked
def todo_checked(request,pk=None):
    todo=get_object_or_404(Todo,id=pk)
    if todo.is_finished==True:
        todo.is_finished=False
    else:
        todo.is_finished=True
    todo.save()
    return redirect('todohome')









