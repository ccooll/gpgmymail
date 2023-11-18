#!/usr/bin/python3
# 
# From ChatGPT 3.5
#

import gnupg
from email import message_from_string
from email.message import Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def encrypt_email(email_data, recipients):
    # Parse the input email
    msg = message_from_string(email_data)

    # Extract the main content of the email
    main_content = None
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            main_content = part.get_payload(decode=True).decode(part.get_content_charset())
            break

    if main_content is None:
        raise ValueError("No plain text part found in the email.")

    # Encrypt the main content using GPG
    gpg = gnupg.GPG(gnupghome="/path/to/your/gnupg/home")
    encrypted_content = gpg.encrypt(main_content, recipients)

    if not encrypted_content.ok:
        raise ValueError(f"Encryption failed: {encrypted_content.status}")

    # Create a new MIMEMultipart object
    encmsg = MIMEMultipart()

    # Copy the original headers
    for key, value in msg.items():
        encmsg[key] = value

    # Attach the encrypted content
    encrypted_part = MIMEText(str(encrypted_content), _subtype="plain", _charset="utf-8")
    encrypted_part["Content-Disposition"] = 'inline; filename="encrypted.asc"'
    encmsg.attach(encrypted_part)

    return encmsg.as_bytes()

# # Example usage:
# with open("input_email.eml", "r") as file:
#     input_email = file.read()

# recipients = ["recipient@example.com"]  # Replace with your recipient's email
# encrypted_email = encrypt_email(input_email, recipients)

# with open("encrypted_email.eml", "wb") as file:
#     file.write(encrypted_email)


