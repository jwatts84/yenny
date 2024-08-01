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

def email_content(email_type):
    if email_type == "wc_claimant_callback":
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


