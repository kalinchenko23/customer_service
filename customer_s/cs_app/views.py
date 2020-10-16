from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,redirect
from .calendar_for_schedule import Calendar
from .models import Schedule
from .forms import SawSome
from .create_issue_pdf import SawSomething
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse
# Create your views here.

x=Calendar()
y=SawSomething()

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

@login_required(login_url='/login')
def saw_something(request):
    form=SawSome()

    if request.method == 'POST':

        form = SawSome(request.POST)
        if form.is_valid():
            issue=form.cleaned_data["issue"]

            y.pdf_built(issue)
            email = EmailMessage(
                'Document',
                'Please see a document attached.',
                'kalinchenko.max@gmail.com',
                ['kalinchenko.97@mail.ru'])
            email.attach_file('/Users/maximkalinchenko/Desktop/customer_service/customer_s/media/issue/issue.pdf')
            email.send()

            messages.success(request, f"The issue was addressed.")
            return redirect("/")


    context={
       "form":form}
    return render(request,"cs_app/see_something_say_something.html",context)

