from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .calendar_for_schedule import Calendar
from .models import Schedule
# Create your views here.

x=Calendar()
@login_required(login_url='/login')
def home(request):
    date=Schedule.objects.all()
    for i in date:
        schedule_date=str(i.date).split("-")
    if int(schedule_date[2]) in x.get_current_month_days():
        event_date=int(schedule_date[2])
        event=[str(i) for i in Schedule.objects.all()]
    else:
        event=""
        event_date=""
    context={'days':x.get_current_month_days(),
            'date':str(date),
            'event_date':event_date,
            'event':event,
            'month_and_year':x.get_current_month_and_year()}
    return render(request, 'cs_app/index.html',context)