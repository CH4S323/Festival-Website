from django.shortcuts import render, redirect
from .models import Festival, Artist, Event, Schedule
from datetime import timedelta
from .forms import TicketForm, MessageForm
from django.http import HttpResponse
# Create your views here.
def home(request):
    festival = Festival.objects.get(pk=1)
    artists = Artist.objects.all()[0:2]
    start = festival.festivalStartDate
    end = festival.festivalEndDate
    
    current = start
    eventOnDays = []
    while current <= end:
        next_day = current + timedelta(days=1)
        eventOnDays.append(Event.objects.filter(festivalName=festival, eventDate__gte=current, eventDate__lt=next_day))

        current = next_day
    
    message = MessageForm()
    if request.method == 'POST':
        message = MessageForm(request.POST)
        if message.is_valid():
            message.save()
            return HttpResponse("Success") #can do any other action

    context = {
        'festival': festival,
        'artists': artists,
        'eventOnDays': eventOnDays,
        'message': message
    }
    return render(request, 'web/index.html', context)

def ticket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success") #can do any other action
    return render(request, 'web/ticket.html', {'form': form})

def test(request):
    schedules = Schedule.objects.all()
    return render(request, 'test.html', {'schedules': schedules})

def login(request):
    return render(request, 'web/LoginRegister.html')