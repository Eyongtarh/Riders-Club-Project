from django.db import models


class ContactMessage(models.Model):
    """
    The model representing a message sent through a contact form with
    attributes of name, email, message, and created_at.
    """
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(max_length=250, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
