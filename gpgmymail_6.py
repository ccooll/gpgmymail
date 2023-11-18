import gnupg
from email import message_from_string
from email.message import Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def encrypt_body(email_data, recipients):
    # Parse the input email
    msg = message_from_string(email_data)

    # Extract the main content of the email
    main_content = msg.get_payload()
    if isinstance(main_content, list):
        # For multipart messages, get the first part
        main_content = main_content[0].get_payload()

    # Encrypt the main content using GPG
    gpg = gnupg.GPG(gnupghome="/path/to/your/gnupg/home")
    encrypted_content = gpg.encrypt(main_content, recipients, always_trust=True)

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

# Example usage:
with open("input_email.eml", "r") as file:
    input_email = file.read()

recipients = ["recipient@example.com"]  # Replace with your recipient's email
encrypted_email = encrypt_body(input_email, recipients)

with open("encrypted_email.eml", "wb") as file:
    file.write(encrypted_email)
