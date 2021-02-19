from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskCreateForms, TaskSearchForms, TaskUpdateForm
# Create your views here.
def create_task(request):
    if request.method == 'GET':
        form = TaskCreateForms()
        tasks = Tasks.objects.filter(status="not completed")

        context = {
            "tasks": tasks,
            "form": form

        }
        return render(request, 'todo/createtask.html', context)
    else:
        form = TaskCreateForms(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data.get('task_name')
            date = form.cleaned_data.get('date')
            status = form.cleaned_data.get('status')

            task = Tasks(task_name=task_name, date=date, status=status)
            task.save()
            tasks = Tasks.objects.all()
            form = TaskCreateForms()
            context = {
                "tasks": tasks,
                "form": form,
            }
            return render(request, 'todo/createtask.html',context)


def search(request):
    if request.method == "GET":
        form = TaskSearchForms()
        context = {
            "form":form
        }

        return render(request, 'todo/tasksearch.html', context)
    else:
        form = TaskSearchForms(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')

            searchs = Tasks.objects.filter(date=date)
            form = TaskSearchForms()

            context = {
                "searchs": searchs,
                "form": form,
            }

            return render(request, 'todo/tasksearch.html', context)




def delete(request, id):
    tasks = Tasks.objects.get(id=id)
    tasks.delete()
    return redirect('create')


def update(request, id):
    tasks = Tasks.objects.get(id=id)

    initial_data = {
        "id": tasks.id,
        "task_name": tasks.task_name,
        "date": tasks.date,
        "status": tasks.status
    }
    form = TaskUpdateForm(initial=initial_data)
    context = {
        "form": form
    }
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data.get('task_name')
            date = form.cleaned_data.get('date')
            status = form.cleaned_data.get('status')
            task = Tasks.objects.get(id=id)
            task.task_name = task_name
            task.date = date
            task.status = status
            task.save()
            return redirect('create')


    return render(request, 'todo/taskupdate.html', context)
