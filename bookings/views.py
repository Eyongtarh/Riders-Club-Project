from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from .forms import BookingForm


class BookingListView(LoginRequiredMixin, ListView):
    """
    This displays a list of bookings for the logged-in user
    and only bookings belonging to the user.
    Pagination is enabled to show 5 bookings per page.
    """
    model = Booking
    context_object_name = 'bookings'
    template_name = 'bookings/booking_list.html'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class BookingDetailView(LoginRequiredMixin, DetailView):
    """
    Here, it displays the details of a specific booking
    for the logged-in user and only bookings belonging to
    the user will be shown.
    """
    model = Booking
    context_object_name = 'booking'
    template_name = 'bookings/booking_detail.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class BookingCreateView(LoginRequiredMixin, CreateView):
    """
    This handles the creation of a new booking and the user will automatically
    be set as the creator of the booking, if positive, a success message is
    displayed.
    """
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('bookings:booking_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Booking created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request,
                       "There was an error creating the booking.")
        return super().form_invalid(form)


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    """
    This takes care of update of an existing booking and only bookings
    belonging to the logged-in user can be updated as well as a success
    message is displayed upon successful update.
    """
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('bookings:booking_list')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Booking updated successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request,
                       "There was an error updating the booking.")
        return super().form_invalid(form)


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    """
    The code here careters for deletion of a booking. Only bookings belonging
    to the logged-in user can be deleted and success message is displayed
    upon successful deletion.
    """
    model = Booking
    template_name = 'bookings/booking_confirm_delete.html'
    success_url = reverse_lazy('bookings:booking_list')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, "Booking deleted successfully.")
        return response
