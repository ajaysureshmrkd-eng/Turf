from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response


from booking.serializer import Userserializer,Trufserializer
from booking.models import Truf

# Create your views here.


class UserAdminCreateView(APIView):

    def post(self,requets):

        form_data =requets.data

        serializer_inst = Userserializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data =serializer_inst.validated_data

            User.objects.create_superuser(**cleaned_data)

            return Response(data=serializer_inst.data)

        else:

            return Response (data=serializer_inst.errors)


class TrufListCreateView(APIView):

    authentication_classes =[authentication.BasicAuthentication]

    permission_classes =[permissions.IsAdminUser]

    def get(self,request):

        qs =Truf.objects.all()

        serializer_inst =Trufserializer(qs,many=True)

        return Response(data=serializer_inst.data)

    def post(self,request):

        form_data =request.data

        serializer_inst =Trufserializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data =serializer_inst.validated_data

            Truf.objects.create(**form_data)

            return Response (data=serializer_inst.validated_data)
        else:

            return Response (data=serializer_inst.errors)


class TrufRetrieveUpdateDeleteView(APIView):

    authentication_classes =[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def get(self,request,pk=None):

        qs =Truf.objects.get(id=pk)

        serializer_inst =Trufserializer(qs)

        return Response (data=serializer_inst.data)

    def put(self,request,pk=None):

        form_data =request.data

        serializer_inst =Trufserializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data =serializer_inst.validated_data

            Truf.objects.filter(id=pk).update()

            return Response(data=serializer_inst.validated_data)

        else:

            return Response(data=serializer_inst.errors)

    def delete(self,request,pk=None):

        qs =Truf.objects.get(id=pk).delete()

        return Response (data={"message":"delete"})

            

            