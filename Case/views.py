from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from .forms import ContactForm, EmailForm, CaseForm
from .models import Contact,Case
from clicksend_comms.utils import send_clicksend_sms_message
from .utils import contact_sms_message

# this is the case homepage
def case_home(request, case_id):
    form = ContactForm()
    contacts = Contact.objects.filter(case_id=case_id)
    context = {'form':form, 'contacts':contacts}
    return render(request, 'wc.html', context)


def ctp(request):
    return render(request, 'ctp.html')

# home page for web app to add and access cases
def home(request):

    if request.method == "POST":
        form = CaseForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            cases = Case.objects.all()
            context = {'form':form, 'cases':cases}
            return render(request,'x_case_div_original.html', context)
        
        else:
            print('FORM NOT VALID')

    else:
        form = CaseForm()
        cases = Case.objects.all()
        context = {'form':form, 'cases':cases}
        return render(request, 'home.html', context)


def x_case_div_update(request, case_id):
    # Retrieve the existing case record or return a 404 if not found
    case = get_object_or_404(Case, id=case_id)
    print(f"Existing case found: {case}")

    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            # Optionally reset the form or provide a success message
            form = CaseForm()
            cases = Case.objects.all()
            context = {'form': form, 'cases': cases, 'case': case}
            return render(request, 'x_case_div_original.html', context)
    else:
        # Initialize the form with the existing case instance
        form = CaseForm(instance=case)
        cases = Case.objects.all()
        context = {'form': form, 'cases': cases, 'case': case}
        return render(request, 'x_case_div_update.html', context)







# CONTACT URLS
def x_contact_div_original(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            contacts = Contact.objects.all()
            context = {'form':form, 'contacts':contacts}
            return render(request,'x_contact_div_original.html', context)
        
        else:
            print('FORM NOT VALID')
    
    else:
        form = ContactForm()
        contacts = Contact.objects.all()
        context = {'form':form, 'contacts':contacts}
        return render(request, 'x_contact_div_original.html', context)



def x_contact_div_update(request, contact_id):
    # update here so it updates the same record not make a new one yip yip

    contact = get_object_or_404(Contact, id=contact_id)
    print(f"Existing contact found: {contact}")
    
    if request.method == 'POST':
        print("Executed here")
        form = ContactForm(request.POST, instance=contact)
        print("this form")
        if form.is_valid():
            form.save()
            form = ContactForm()
            contacts = Contact.objects.all()
            context = {'form':form, 'contacts':contacts, 'contact':contact}
            return render(request, 'x_contact_div_original.html', context)

    
    else:
        # contact = get_object_or_404(Contact, id=contact_id)
        form = ContactForm(instance=contact)
        contacts = Contact.objects.all()
        context = {'form':form, 'contacts':contacts, 'contact':contact}
        return render(request, 'x_contact_div_update.html', context)
    

def x_contact_delete(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    form = ContactForm()
    contacts = Contact.objects.all()
    context = {'form':form, 'contacts':contacts}
    return render(request, 'x_contact_div_original.html', context)

    # update here so it updates the same record not make a new one yip yip


def contact_sms(request, contact_id):
    contact = get_object_or_404(Contact,id=contact_id)
    case = contact.case
    contacts = Contact.objects.all()
    form = ContactForm()

    if request.method == "POST":
        message_type = request.POST["type"]
        details = {
            'name':contact.first_name,
            'claimant':case.claimant
        }
        phone = contact.phone
        message = contact_sms_message(message_type,details)
        print(f"this is your message: {message}")

        send_clicksend_sms_message(phone, message)

        context = {'form':form, 'contacts':contacts}
        return render(request, 'x_contact_div_original.html', context)

    else:
        context = {'contact':contact, 'contacts':contacts}
        return render(request, 'x_contact_div_sms.html', context)
        









