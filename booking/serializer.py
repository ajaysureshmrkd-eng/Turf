from rest_framework import serializers

from booking.models import Truf


class Userserializer(serializers.Serializer):

    username =serializers.CharField()

    email =serializers.EmailField()

    password =serializers.CharField()

class Trufserializer(serializers.Serializer):

    id =serializers.CharField(read_only=True)

    name =serializers.CharField()

    location =serializers.CharField()

    phone =serializers.IntegerField()

    fee =serializers.IntegerField()

    def validate(self,validated_data):

        fee =validated_data.get("fee")

        if fee<800:

            raise serializers.ValidationError("invalid fee,fee should be >800")

        else:

            return validated_data


        
    