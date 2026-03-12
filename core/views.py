from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone


@login_required
def dashboard(request):
    return render(request, "dashboard.html", {
        "now": timezone.now()
    })