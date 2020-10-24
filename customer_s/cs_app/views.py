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
from .uniform_selector import uniform
import datetime
# Create your views here.

x=Calendar()
y=SawSomething()
today=str(datetime.date.today())
@login_required(login_url='/login')
def home(request):
    today_split=int(str(datetime.date.today()).split("-")[2])
    dat=Schedule.objects.all()
    d=[(int(str(i.date).split("-")[2]),i.name) for i in dat]


    event=""

    context={'days':x.get_current_month_days(),
            'uniform':uniform,
            'today_split':today_split,
            'd':d,
            'today':today,
            'dat':dat,
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

