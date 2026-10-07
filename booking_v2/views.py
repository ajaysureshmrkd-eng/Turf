from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions

from booking_v2.serializers import SignUpserializer,bookingserializer
from django.contrib.auth.models import User
from booking_v2.models import booking

from datetime import date,timedelta,datetime

class SignUpView(APIView):

    def post(self,request):

        form_data =request.data

        serializer_inst =SignUpserializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data =serializer_inst.validated_data

            user_object =User.objects.create_user(**cleaned_data)

            serializer_inst =SignUpserializer(user_object)

            return Response (data=serializer_inst.data)

        else:

            return Response (data= serializer_inst.errors)


class BookingListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,reqest):

        qs =booking.objects.all()

        serializer_inst=bookingserializer(qs,many=True)

        return Response (data=serializer_inst.data)

    def post(self,request):

        form_data =request.data

        serializer_inst = bookingserializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data =serializer_inst.validated_data

            turf =cleaned_data.get("turf")

            date =cleaned_data.get("date")

            start_time =cleaned_data.get("start_time")

            match_duration =cleaned_data.get("match_duration")

            start_datetime =datetime.combine(date,start_time)

            end_datetime =start_datetime +match_duration

            end_time =end_datetime.time()

            exist_booking=booking.objects.filter(date=date,start_time__lt=end_time,end_time__gt=start_time).exists()

            if exist_booking:

                return Response(data={"error":"turf is already booked"})

            cleaned_data["end_time"]=end_time

            new_booking=booking.objects.create(**cleaned_data)

            serializer_inst =bookingserializer(new_booking)

            return Response (data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)


class BookingRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class =bookingserializer

    queryset =booking.objects.all()





            




            









