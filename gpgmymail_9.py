import gnupg
from email import message_from_string

def get_text_payload(msg):
    if msg.is_multipart():
        for part in msg.get_payload():
            if part.get_content_type() == 'text/plain':
                return part.get_payload(decode=True).decode(part.get_content_charset())
            elif part.get_content_type() == 'text/html':
                # If plain text part is not found, use HTML content
                return part.get_payload(decode=True).decode(part.get_content_charset())
    else:
        return msg.get_payload(decode=True).decode(msg.get_content_charset())

def encrypt_body(email_data, recipients):
    # Parse the input email
    msg = message_from_string(email_data)

    # Extract the main content of the email
    main_content = get_text_payload(msg)

    # Encrypt the main content using GPG
    gpg = gnupg.GPG(gnupghome="/path/to/your/gnupg/home")
    encrypted_content = gpg.encrypt(main_content, recipients, always_trust=True)

    if not encrypted_content.ok:
        raise ValueError(f"Encryption failed: {encrypted_content.status}")

    # Construct the encrypted email
    headers = str(msg)[:str(msg).find(main_content)].strip()
    encrypted_email = f"{headers}\n\n{encrypted_content}"

    return encrypted_email

# Example usage:
with open("input_email.eml", "r") as file:
    input_email = file.read()

recipients = ["recipient@example.com"]  # Replace with your recipient's email
encrypted_email = encrypt_body(input_email, recipients)

with open("encrypted_email.eml", "w") as file:
    file.write(encrypted_email)
