from django.shortcuts import render

from .models import Passcard, Visit


def active_passcards_view(request):
    all_passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': active_passcards,
    }
    return render(request, 'active_passcards.html', context)
