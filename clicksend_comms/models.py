from django.db import models


class ClickSendEmail(models.Model):
    # description gives engineer understanding of
    # what the email is about
    description = models.TextField()
    # email_address_id = models.CharField() is the id
    # associated with the email in clicksend
    email_address_id = models.CharField(max_length=250)
    email_from_name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    content = models.TextField()
