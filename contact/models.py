from django.db import models


class ContactMessage(models.Model):
    """
    Model representing a message sent through a contact form.

    Attributes:
        name (str): The name of the person sending the message.
        email (str): The email address of the sender.
        message (str): The content of the message (limited to 250 characters).
        created_at (datetime): Timestamp of when the message was created
        (auto-generated).
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the contact message,
        typically the sender's name.
        """
        return self.name
