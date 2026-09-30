from rest_framework import serializers


class BookingSlotserializer(serializers.Serializer):

    customer_name =serializers.CharField()

    phone =serializers.IntegerField()

    turf =serializers.IntegerField()

    booking_date =serializers.DateField()

    booking_time =serializers.TimeField()

    duration =serializers.IntegerField()

    email =serializers.EmailField()



