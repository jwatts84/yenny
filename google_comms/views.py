from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from .models import UserCredentials
from .utils import build_service

def oauth2_start(request):
    flow = Flow.from_client_secrets_file(
        'google_client_secret.json',
        scopes=['https://www.googleapis.com/auth/contacts'],
        redirect_uri=request.build_absolute_uri(reverse('oauth2_callback'))
    )
    authorization_url, state = flow.authorization_url()
    request.session['state'] = state
    return redirect(authorization_url)

def oauth2_callback(request):
    state = request.session['state']


    flow = Flow.from_client_secrets_file(
        'google_client_secret.json',
        scopes=['https://www.googleapis.com/auth/contacts'],
        state=state,
        redirect_uri=request.build_absolute_uri(reverse('oauth2_callback'))
    )
    # seems to need HTTPS request for it to work ok
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials

    # Save credentials to the database
    UserCredentials.objects.update_or_create(
        user=request.user,
        defaults={
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': ",".join(credentials.scopes),
        }
    )
    
    return redirect('contacts_home')



def create_contact(request):

    try:
        user_credentials = UserCredentials.objects.get(user=request.user)
    
    except:
        return redirect('oauth2_start')
    
    service = build_service(request.user)
    
    try:
        contact = service.people().createContact(body={
            "names": [
                {"givenName": "John", "familyName": "Doe"}
            ],
            "phoneNumbers": [
                {'value': "1234567890"}
            ],
            "emailAddresses": [
                {'value': 'johndoe@example.com'}
            ]
        }).execute()

        return HttpResponse("contact added")
    except HttpError as e:
        print(e)
        return HttpResponse("did not work")

