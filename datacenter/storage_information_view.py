from datetime import timedelta

from django.shortcuts import render

from datacenter.models import Visit


def format_duration(duration):
    total_seconds = timedelta.total_seconds(duration)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return '{0}ч {1}мин'.format(int(hours), int(minutes))


def storage_information_view(request):
    non_closed_visits = []
    context = {
        'non_closed_visits': non_closed_visits,
    }
    not_leaved = Visit.objects.filter(leaved_at__isnull=True)
    for visitor in not_leaved:
        non_closed_visits.append(
            {
                'who_entered': visitor.passcard,
                'entered_at': visitor.get_time_entered_localtime(),
                'duration': format_duration(visitor.get_duration())
            }
        )

    return render(request, 'storage_information.html', context)
