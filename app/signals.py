from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Customer

@receiver(pre_delete, sender=Customer)
def before_delete_customer(sender, instance, **kwargs):
    customer_email = instance.email
    subject = 'Customer account deletion'
    message = f'Dear {instance.name}, your account will be deleted shortly.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [customer_email]
    send_mail(subject, message, from_email, recipient_list)
