from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking, Turf
from django.contrib import messages

@login_required
def book_turf(request):
    if request.method == "POST":
        turf_id = request.POST.get("turf")
        date = request.POST.get("date")
        time_slot = request.POST.get("time_slot")

        turf = Turf.objects.get(id=turf_id)
        Booking.objects.create(user=request.user, turf=turf, date=date, time_slot=time_slot)

        messages.success(request, "Booking confirmed!")
        return redirect("booking_list")

    turfs = Turf.objects.all()
    return render(request, "bookings/book_turf.html", {"turfs": turfs})

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "bookings/booking_list.html", {"bookings": bookings})