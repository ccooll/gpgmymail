import gnupg
from email import message_from_string

def encrypt_body(email_data, recipients):
    # Parse the input email
    msg = message_from_string(email_data)

    # Extract the main content of the email
    main_content = msg.get_payload()
    if isinstance(main_content, list):
        # For multipart messages, concatenate the payload parts
        payload_parts = [part.get_payload() for part in main_content]
        main_content = '\n'.join(payload_parts)

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
