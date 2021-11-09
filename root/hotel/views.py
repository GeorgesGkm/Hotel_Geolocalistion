from django.shortcuts import render
from django.views.generic.base import TemplateView


from .models import Hotel
from .forms import HotelForm

from .serializers import HotelSerialzer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
class Home(TemplateView):
    template_name = 'rooms/rooms.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['rooms'] = Hotel.objects.all()
        return context


def add_hotels(request, *args, **kwargs):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    form = HotelForm()
    ctx = {'form': form, }
    return render(request, 'rooms/room.html', ctx)


@api_view(['GET'])
def hotelsApi(request, *args, **kwargs):
    hotels = Hotel.objects.all()
    data = HotelSerialzer(hotels, many=True).data
    return Response(data)
