from django.shortcuts import render
from .forms import ContactMessageForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    else:
        form = ContactMessageForm()
    return render(request, 'contact/contact_form.html', {'form': form})
