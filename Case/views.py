from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from .forms import ContactForm, EmailForm, CaseForm
from .models import Contact,Case, Note
from clicksend_comms.utils import send_clicksend_sms_message
from .utils import contact_sms_message, generate_email_content
from django.utils import timezone
from AI.models import TwoShotPrompt
from AI.utils import langchain_two_shot

# this is the case homepage
def case_home(request, case_id):
    form = ContactForm()
    contacts = Contact.objects.filter(case_id=case_id)
    context = {'form':form, 'contacts':contacts, 'case_id':case_id}
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
        # clicksend
        message_type = request.POST["type"]
        details = {
            'name':contact.first_name,
            'claimant':case.claimant
        }
        phone = contact.phone
        message = contact_sms_message(message_type,details)
        send_clicksend_sms_message(phone, message)

        # add sms as note
        note_message = f"SMS TEXT MESSGAGE SENT TO: {contact.first_name} {contact.last_name}" + message 
        note = Note.objects.create(
            contact_id=contact_id,
            note=note_message,
            created_at = timezone.now()
        )

        context = {'form':form, 'contacts':contacts}
        return render(request, 'x_contact_div_original.html', context)
    


    else:
        context = {'contact':contact, 'contacts':contacts}
        return render(request, 'x_contact_div_sms.html', context)
    
def contact_email(request, contact_id):

    contact = get_object_or_404(Contact,id=contact_id)
    case = contact.case
    contacts = Contact.objects.all()
    form = ContactForm()

    if request.method == "POST":
        message = request.POST["message_body"]
        print(f"this is message body: {message}")
        note = Note.objects.create(
            contact_id=contact_id,
            note=message,
            created_at = timezone.now()
            )
        context = {'contacts':contacts, 'form':form}
        return render(request, 'x_contact_div_original.html', context)

    else:
        context = {'contact':contact, 'contacts':contacts, 'form':form}
        return render(request, 'x_contact_div_email.html', context)
        

def email_content(request, contact_id):

    contact = Contact.objects.get(id=contact_id)
    contacts = Contact.objects.all()
    case = contact.case
    form = ContactForm()

    if request.method == "GET":
        details = {
            'name':contact.first_name,
            'claimant':case.claimant,
            'email': contact.email,
            }

        email_type = request.GET.get('email_type')
        print(f"this is the email type : {email_type}")
        email = generate_email_content(email_type,details)
        context = {'email':email}

        return render(request, 'partial_email_body.html', context)
    
    if request.method == "POST":
        
        message = request.POST["message_body"]
        print(f"this is message body: {message}")
        note =Note.object.create(
            contact_id=contact_id,
            note=message,
            created_at = timezone.now()
            )
        
        context = {'contacts':contacts, 'form':form}
        return render(request, 'x_contact_div_original.html', context)
    

def contact_note(request, contact_id):

    contact = get_object_or_404(Contact,id=contact_id)
    case = contact.case
    contacts = Contact.objects.all()
    form = ContactForm()

    if request.method == "POST":
        message = request.POST["note_body"]
        print(f"this is message body: {message}")
        message = f"NOTE regarding {contact.first_name} {contact.last_name}" + message
        print(f"this is message body: {message}")
        note = Note.objects.create(
            contact_id=contact_id,
            note=message,
            created_at = timezone.now()
            )
        context = {'contacts':contacts, 'form':form}
        return render(request, 'x_contact_div_original.html', context)

    else:
        context = {'contact':contact, 'contacts':contacts, 'form':form}
        return render(request, 'x_contact_div_note.html', context)



def case_ai(request,case_id):

    raw_prompt = TwoShotPrompt.objects.get(id=1).get_prompt("my prompt")

    ai_result = langchain_two_shot(raw_prompt)

    context = {'ai_result':ai_result}

    return render(request, 'partial_ai_result_textarea.html', context)



    


    












