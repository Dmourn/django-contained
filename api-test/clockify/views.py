from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import permissions, generics, viewsets, renderers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

#adding django-oauth-toolkit authentication
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope, TokenHasScope

from rest_framework.views import APIView
from oauth2_provider.views.generic import ProtectedResourceView, ClientProtectedResourceView

from .serializers import AccountsSerializer, ContactsSerializer, ClockifyClientSerializer, ClockifyTimeEntrySerializer, ClockifyTimeEntrySerializer, ClockifyProjectSerializer
from .models import Accounts, Contacts, ClockifyClient, ClockifyTimeEntry, ClockifyProject

from .auth.clockify import ClockifyAuthentication


#Zoho Contacct
class ContactsList(APIView):
    authentication_classes = [SessionAuthentication, OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]

    def get(self, request):
        contacts = Contacts.objects.all()
        serializer = ContactsSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        #data = JSONParser().parse(request)
        #print(data)
        serializer = ContactsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            json = renderers.JSONRenderer().render(serializer.data)
            print(serializer.data)
            print(json)
            print(request.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)
#Zoho Account
class AccountsList(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]

    def get(self, request, **kwargs):
        data = request.data
        print(data)
        if data:
            try:
                queryset = Accounts.objects.all().filter(account_id=data['account_id'])
                print('hit query statement')
            except:
                print(f'{data} data does not have accountid')
                queryset = Accounts.objects.all()
        else:
            queryset = Accounts.objects.all()
        serializer = AccountsSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = AccountsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            json = renderers.JSONRenderer().render(serializer.data)
            print(serializer.data)
            print(json)
            print(request.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#class AccountsDetailView(generics.GenericAPIView):
class AccountsDetailView(generics.RetrieveAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]
    lookup_field = 'account_id'
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

class ClockifyClientList(APIView):
    authentication_classes = [ClockifyAuthentication]
    #authentication_classes = [OAuth2Authentication]
    permission_classes = [permissions.IsAuthenticated]
    
    #permission_classes = [TokenHasReadWriteScope]

    def get(self, request, **kwargs):
        data = request.data
        print(data)
        if data:
            try:
                queryset = ClockifyClient.objects.all().filter(id=data['id'])
                print(f'hit query statement: {queryset}')
            except:
                print(f'{data} data does not have accountid')
                queryset = ClockifyClient.objects.all()
        else:
            queryset = ClockifyClient.objects.all()
        serializer = ClockifyClientSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        """
        print(f'dir(request): {dir(request)}')
        try:
            print(request.META)
            websec = request.META['HTTP_CLOCKIFY_SIGNATURE']
            print(websec)
        except:
            print('clockify-signature not found in request.META')

        """

        #print(f'{request.META["HTTP_CLOCKIFY_SHIT"]}')
        #print(f'dir keys: {request.query_params.keys()}')
        serializer = ClockifyClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            json = renderers.JSONRenderer().render(serializer.data)
            print(serializer.data)
            print(json)
            print(request.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ClockifyClientDetailView(generics.RetrieveAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]
    lookup_field = 'id'
    queryset = ClockifyClient.objects.all()
    serializer_class = ClockifyClientSerializer

class ClockifyTimeEntryList(APIView):
    authentication_classes = [ClockifyAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs):
        data = request.data
        if data:
            try:
                queryset = ClockifyTimeEntry.objects.all().filter(id=data['id'])
            except:
                print(f'{data} data does not have accountid')
                queryset = ClockifyTimeEntry.objects.all()
        else:
            queryset = ClockifyTimeEntry.objects.all()
        serializer = ClockifyTimeEntrySerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        #data['timeId']=data['id']
        serializer = ClockifyTimeEntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            json = renderers.JSONRenderer().render(serializer.data)
            print(serializer.data)
            print(json)
            print(request.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ClockifyProjectCreateList(generics.ListCreateAPIView):
    authentication_classes = [ClockifyAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    queryset = ClockifyProject.objects.all()
    serializer_class = ClockifyProjectSerializer

class ClockifyTimeEntryCreateList(generics.ListCreateAPIView):
    authentication_classes = [ClockifyAuthentication]
    #authentication_classes = [OAuth2Authentication]
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [OAuth2Authentication]
    #permission_classes = [TokenHasReadWriteScope]
    
    queryset = ClockifyTimeEntry.objects.all()
    serializer_class = ClockifyTimeEntrySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
