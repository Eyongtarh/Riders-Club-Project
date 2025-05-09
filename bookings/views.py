from django.shortcuts import render, get_object_or_404, redirect
from .models import TrainingSession
from .forms import TrainingSessionForm
from django.contrib.auth.decorators import login_required


@login_required
def training_session_list(request):
    sessions = TrainingSession.objects.all()
    return render(request,
                  'training_sessions/session_list.html',
                  {'sessions': sessions})


@login_required
def training_session_create(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('session_list')
    else:
        form = TrainingSessionForm()
    return render(request,
                  'training_sessions/session_form.html', {'form': form})


@login_required
def training_session_update(request, pk):
    session = get_object_or_404(TrainingSession, pk=pk)
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('session_list')
    else:
        form = TrainingSessionForm(instance=session)
    return render(request,
                  'training_sessions/session_form.html', {'form': form})


@login_required
def training_session_delete(request, pk):
    session = get_object_or_404(TrainingSession, pk=pk)
    if request.method == 'POST':
        session.delete()
        return redirect('session_list')
    return render(request,
                  'training_sessions/session_confirm_delete.html',
                  {'session': session})
