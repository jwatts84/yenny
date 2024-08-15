def contact_sms_message(msg_type, details):
    name = details["name"]
    claimant = details["claimant"]
    
    if msg_type == "wc_claimant_callback":
        message = (f"Hello {name},\n"
                   f"Can you please call me at your earliest convenience in relation to "
                   f"your workers compensation claim on 0476 209 802.\n"
                   f"Kind regards,\n"
                   f"Jesse Watts")
        
    else:
        message = (f"Hello {name},\n"
                   f"Can you please call me at your earliest convenience in relation to "
                   f"{claimant}'s workers compensation claim on 0476 209 802.\n"
                   f"Kind regards,\n"
                   f"Jesse Watts")

    
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


