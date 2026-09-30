from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from turf_slot.models import BookingSlot 
from turf_slot.serializers import BookingSlotserializer

# Create your views here.

class BookingSlotListCreateView(APIView):

    def get(self,request):

        qs =BookingSlot.objects.all()

        serializer_inst =BookingSlotserializer(qs,many=True)

        return Response(data=serializer_inst.data)
        