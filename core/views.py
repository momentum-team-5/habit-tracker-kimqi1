from django.shortcuts import render
from datetime import date
from core.models import Habit
from core.models import record

# Create your views here.

# Create one habit
def add_habit(request):
    if request.method == "GET":
        form = HabitForm()

    else:
        form = HabitForm(data=request.POST)

        if form.is_valid():
            habit = form.save()
            return redirect("habit-detail" , pk=habit.pk)
    return render(request, "core/habit_create.html", {"form": form})


# Show one habit
def habit_detail(request, pk):
    habit = get_object_or_404(habit, pk=pk)
    return render(request, "habit/habits_list.html", {"habits": habits})


# Update one habit
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == "GET":
        form = HabitForm(instance=form)

    else:
        form = HabitForm(data=request.POST)

        if form.is_valid():
            habit = form.save()  

            return redirect("habit-detail", pk=habit.pk


    return render(request, "habit/edit_habit.html", {"habit": habit, "form": form})



# list all habits
def habit_list(request):
    habits = habit.objects.all()

    return render(request, "habit/habits_list.html", {"habits": habits})



# delete a habit
def delete_habit(request, pk):
    habit = get_object_or_404(Poem, pk=pk)

    if request.method == "POST"
        habit.delete()
        return redirect("habit-list")

    return render(request, "core/habit_delete.html", {"habit": habit})

    

# create a record


# update a record


# delete a record




