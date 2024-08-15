from .models import Case, Contact

def contact_sms_message(msg_type, details):
    name = details["name"]
    claimant = details["claimant"]
    
    if msg_type == "wc_claimant_callback":
        message = (f"Hello {name},\n\n"
                   f"Can you please call me at your earliest convenience in relation to "
                   f"your workers compensation claim on 0476 209 802.\n\n"
                   f"Kind regards,\n\n"
                   f"Jesse Watts")
        
    elif msg_type == "ctp_callback":
        message = (f"Hello {name},\n\n"
                   f"Can you please call me at your earliest convenience"
                   f"on 0476 209 802.\n\n"
                   f"Kind regards,\n\n"
                   f"Jesse Watts")
  
    elif msg_type == "wc_witness_callback":
        message = (f"Hello {name},\n\n"
                   f"Can you please call me at your earliest convenience on 0476 209 802"
                   f"in relation to a workers compensation matter you can assist with.\n\n"
                   f"Kind regards,\n\n"
                   f"Jesse Watts")
        
    else:
        pass

    
    return message

def generate_email_content(email_type, details):
    name = details["name"]
    claimant = details["claimant"]
    email = details["email"]


    if email_type == "wc_claimant_callback":
        message = (f"Hello {email},\n\n"
                   f"Hello {name},\n"
                   f"Can you please call me at your earliest convenience in relation to "
                   f"your workers compensation claim on 0476 209 802.\n"
                   f"Kind regards,\n"
                   f"Jesse Watts")
        
    elif email_type == "wc_witness_callback":
        message = (f"EMAIL: {email}\n\n"
                   f"SUBJECT LINE: {claimant} | Workers Comp Matter\n\n"
                   f"Hello {name},\n\n"
                   f"Can you please call me at your earliest convenience in relation to {claimant}'s workers compensation claim on 0476 209 802.\n\n"
                   f"We received your details from your employer in relation to this matter.\n\n"
                   f"Kind regards,\n")

        
    else:
        message = "select an email type above"

    return message


def create_case_file_note_contact(case):
    case_id = case.id

    # Create a contact associated with the case_id
    Contact.objects.create(
        case_id=case_id,
        type="other",
        first_name="FILE",
        last_name="NOTE"
    )




