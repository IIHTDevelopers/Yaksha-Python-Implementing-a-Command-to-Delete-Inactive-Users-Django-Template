# views.py
from django.shortcuts import render
from .models import Event

def event_list(request):
    # Use select_related or prefetch_related to optimize database queries
    events = Event.objects.all().prefetch_related('participants')
    eve = list(events)
    return render(request, 'blog_detail.html', {'events': events})
