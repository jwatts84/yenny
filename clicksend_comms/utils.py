from __future__ import print_function
import os
import requests
import base64


# third party libraries
import clicksend_client
from clicksend_client.rest import ApiException
from clicksend_client import EmailRecipient
from clicksend_client import EmailFrom
from clicksend_client import Attachment
from clicksend_client import PostRecipient

# keys
click_user_key = os.getenv("CLICKSEND_API_USERNAME")
clicksend_password_key = os.getenv("CLICKSEND_API_KEY")


# SEND EMAIL
def send_clicksend_email(
    recipient_email,
    recipient_name,
    clicksend_email_from_id,
    email_from_name,
    email_subject,
    email_body,
):
    # NOTE: clicksend_email_from_id is in clicksend portal and corresponds to sender (from) email
    # configuration
    configuration = clicksend_client.Configuration()
    configuration.username = click_user_key
    configuration.password = clicksend_password_key
    # create an instance of the API class
    api_instance = clicksend_client.TransactionalEmailApi(
        clicksend_client.ApiClient(configuration)
    )
    email_receipient = EmailRecipient(email=recipient_email, name=recipient_name)
    email_from = EmailFrom(
        email_address_id=clicksend_email_from_id, name=email_from_name
    )
    # Email | Email model
    email = clicksend_client.Email(
        to=[email_receipient],
        _from=email_from,
        subject=email_subject,
        body=email_body,
    )
    try:
        # Send transactional email
        api_response = api_instance.email_send_post(email)
        print(api_response)
        return True
    except ApiException as e:
        print("Exception when calling TransactionalEmailApi->email_send_post: %s\n" % e)


def send_clicksend_sms_message(recipient_phone_number, desired_message_to_recipient):
    # get request url
    url = f"https://api-mapper.clicksend.com/http/v2/send.php?method=http&username={click_user_key}&key={clicksend_password_key}&to={recipient_phone_number}&message={desired_message_to_recipient}&senderid=Jesse"
    # sends the sms via get request
    response = requests.get(url)
    # Check the response
    if response.status_code == 200:
        print("SMS sent successfully!")
    else:
        print("Failed to send SMS. Response:", response.text)


def send_clicksend_physical_mail(recipient_details):


    # Configure HTTP basic authorization: BasicAuth
    configuration = clicksend_client.Configuration()
    # PUT CORRECT KEYS BELOW
    configuration.username = click_user_key
    configuration.password = clicksend_password_key
     

    # create an instance of the API class
    api_instance = clicksend_client.PostLetterApi(clicksend_client.ApiClient(configuration))
    post_recipient=PostRecipient(
                address_name=recipient_details['name'],
                address_line_1=recipient_details['street_address'],
                address_line_2="",
                address_city= recipient_details['suburb'],
                address_state=recipient_details['state'],
                address_postal_code=recipient_details['postal_code'],
                address_country="AU",
                return_address_id=701421,
                # 0 sends letter now
                schedule=0)
    
    # PostLetter | PostLetter model
    # NOTE THE FILE CAN BE A DOCX!!!!!  https://help.clicksend.com/article/wcpkkoou6c-post-letter-template
    post_letter = clicksend_client.PostLetter(
                file_url=recipient_details['file_url'],
                template_used= 0,
                colour=1,
                duplex=0,
                recipients=[post_recipient]) 

    try:
        # Send post letter
        api_response = api_instance.post_letters_send_post(post_letter)
        print(api_response)
    except ApiException as e:
        print("Exception when calling PostLetterApi->post_letters_send_post: %s\n" % e)



