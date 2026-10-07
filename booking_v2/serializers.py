from rest_framework import serializers

from booking_v2.models import booking

from django.contrib.auth.models import User

from datetime import datetime



class bookingserializer(serializers.ModelSerializer):

    class Meta:

        model =booking

        fields ="__all__"

        read_only_fields =["id","end_time"]

    def validate(self, validated_data):

        date =validated_data.get("date")

        if date <datetime.today().date():

            raise serializers.ValidationError("invalid booking date.pls enter a valid future date")

        return validated_data


class SignUpserializer(serializers.ModelSerializer):

    class Meta:

        model =User

        fields =["username","email","password"]


