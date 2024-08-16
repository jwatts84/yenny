from googleapiclient.discovery import build
from .models import UserCredentials

def build_service(user):
    user_credentials = UserCredentials.objects.get(user=user)
    credentials = user_credentials.to_credentials()
    service = build('people', 'v1', credentials=credentials)
    return service
