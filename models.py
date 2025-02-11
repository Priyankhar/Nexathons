from django.db import models
from django.contrib.auth.models import User

class Turf(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username} - {self.turf.name} on {self.date} at {self.time_slot}"

class BookingMessage(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    confirmation_message = models.TextField()
    alert_sent = models.BooleanField(default=False)
    def _str_(self):
        return f"Message for {self.booking}"