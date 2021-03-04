from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import TimerForm
from .models import Timer


# Create your views here.
def create_timer(request):
    template = loader.get_template('index.html')
    form = TimerForm(request.GET or None)
    if request.POST:
        form = TimerForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']
            Timer.objects.create(
                start=start,
                end=end
            )
    timers = Timer.objects.all()
    context = {
        'form': form,
        'timers': timers
    }

    return HttpResponse(template.render(context, request))
