
from core.models import Habit, Record
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from core.forms import HabitForm


# Create your views here.

# list all habits
@login_required(login_url='/accounts/login')
def habit_list(request):
    habits = Habit.objects.all()

    return render(request, "core/habit_list.html", {"habits": habits})

# Show deatails of one habit
@login_required(login_url='/accounts/login')
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, "core/habit_list.html", {"habit": habit})

# Create habit
@login_required(login_url='/accounts/login')
def add_habit(request):
    if request.method == "GET":
        form = HabitForm()

    else:
        form = HabitForm(data=request.POST)

        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect("habit_detail", pk=habit.pk)
    return render(request, "core/habit_create.html", {"form": form})


# update habit
@login_required(login_url='/accounts/login')
def update_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == "GET":
        form = HabitForm(instance=habit)

    else:
        form = HabitForm(instance=habit, data=request.POST)

        if form.is_valid():
            habit = form.save() 

            return redirect("habit_detail", pk=habit.pk)


    return render(request, "habit/edit_habit.html", {"habit": habit, "form": form})



# delete a habit
@login_required(login_url='/accounts/login')
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == "POST":
        habit.delete()
        return redirect("habit_list")

    return render(request, "core/habit_delete.html", {"habit": habit})


# create a record
#@login_required(login_url='/accounts/login')

#class Meta:
#    unique_together = ["user", "date",]


# update a record
#@login_required(login_url='/accounts/login')


# delete a record
#@login_required(login_url='/accounts/login')
