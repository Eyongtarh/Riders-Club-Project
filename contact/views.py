from django.shortcuts import render
from .forms import ContactMessageForm


def contact_view(request):
    """
    Takes care of contact form submissions.
    If post request is validated and if form is valid,
    form is saved and render a success page.
    """
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    else:
        form = ContactMessageForm()
    return render(request, 'contact/contact_form.html', {'form': form})
