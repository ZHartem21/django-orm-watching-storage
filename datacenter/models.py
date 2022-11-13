from datetime import timedelta

import django.utils.timezone
from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_time_entered_localtime(self):
        return django.utils.timezone.localtime(self.entered_at)

    def get_duration(self):
        if not self.leaved_at:  
            current_time = django.utils.timezone.localtime()
            time_delta = current_time - django.utils.timezone.localtime(
                self.entered_at
            )
            return time_delta
        time_delta_finished_visit = self.leaved_at - self.entered_at
        return time_delta_finished_visit

    def is_visit_long(self, minutes):
        return (timedelta.total_seconds(self.get_duration()) // 60) >= minutes