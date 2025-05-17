from django.shortcuts import render
from .forms import ContactMessageForm


def contact_view(request):
    """
    Handle contact form submissions.

    - If the request method is POST, validate the submitted form data.
      - If valid, save the form and render a success page.
    - If the request method is not POST (typically GET), render an empty form.

    Template used:
    - contact/contact_form.html: for displaying the form.
    - contact/success.html: for showing a success message after submission.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page based on form state.
    """
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    else:
        form = ContactMessageForm()
    return render(request, 'contact/contact_form.html', {'form': form})
