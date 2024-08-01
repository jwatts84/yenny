from django.urls import path
from . import views

urlpatterns = [
    # case_home_page
    path('<int:case_id>', views.case_home, name="case_home"),
    path('edit/<int:case_id>', views.x_case_div_update, name="x_case_div_update"),

    # CONTACT URLS
    # htmx 
    path('contact', views.x_contact_div_original, name="x_contact_div_original"),
    path('contact/edit/<int:contact_id>', views.x_contact_div_update, name="x_contact_div_update"),
    path('contact/delete/<int:contact_id>', views.x_contact_delete, name="x_contact_delete"),

    # communication
    path('contact/sms/<int:contact_id>', views.contact_sms, name="x_contact_div_sms"),
    path('contact/email/<int:contact_id>', views.contact_email, name="x_contact_div_email"),
    path('contact/email_content', views.email_content, name="x_email_content"),

]



