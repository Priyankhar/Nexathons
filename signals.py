from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Booking, BookingMessage

@receiver(post_save, sender=Booking)
def send_booking_confirmation(sender, instance, created, **kwargs):
    if created:
        message = f"Dear {instance.user.username},\n\n" \
                  f"Your booking for {instance.turf.name} on {instance.date} at {instance.time_slot} is confirmed.\n\n" \
                  f"Thank you for choosing us!"

      
        BookingMessage.objects.create(booking=instance, confirmation_message=message)

        
        send_mail(
            'Booking Confirmation',
            message,
            'your_email@gmail.com', 
            [instance.user.email],
            fail_silently=False,
        )