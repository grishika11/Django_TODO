from django.shortcuts import render,redirect
from .models import Task,Dear
from .forms import TaskForm, DearForm
# Create your views here.
def Index(request):
	tasks  = Task.objects.all()
	form = TaskForm()
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	context = {'tasks':tasks,'form':form}

	return render(request,'index.html',context)


def UpdateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('index')

	context = {'form':form}

	return render(request, 'update.html', context)


def DeleteTask(request,pk):
	item = Task.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('index')

	context = {'item':item}
	return render(request,'delete.html',context)


def Dear1(request):
	dears  = Dear.objects.all()
	form = DearForm()
	if request.method =='POST':
		form = DearForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dairy')
	context = {'dears':dears,'form':form}

	return render(request,'dairy.html',context)

def Next(request):
	return render(request,'next.html')
