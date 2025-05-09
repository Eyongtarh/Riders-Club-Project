from django.shortcuts import render, redirect, get_object_or_404
from .models import TrainingSession
from .forms import TrainingSessionForm
from django.contrib.auth.decorators import login_required


@login_required
def session_list(request):
    sessions = TrainingSession.objects.filter(author=request.user)
    return render(request,
                  'bookings/session_list.html', {'sessions': sessions})


@login_required
def session_create(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.author = request.user
            session.save()
            return redirect('session_list')
    else:
        form = TrainingSessionForm()
    return render(request, 'bookings/session_form.html', {'form': form})


@login_required
def session_update(request, pk):
    session = get_object_or_404(TrainingSession, pk=pk, author=request.user)
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('session_list')
    else:
        form = TrainingSessionForm(instance=session)
    return render(request, 'bookings/session_form.html', {'form': form})


@login_required
def session_delete(request, pk):
    session = get_object_or_404(TrainingSession, pk=pk, author=request.user)
    if request.method == 'POST':
        session.delete()
        return redirect('session_list')
    return render(request,
                  'bookings/session_confirm_delete.html', {'session': session})
