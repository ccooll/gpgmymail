# gpgmymail

The original Idea came from looking at Julian Andres Klode blog's at https://blog.jak-linux.org/2019/06/13/encrypted-email-storage/
I used, which I modified a bit, and added the missing part to be integrated in my mail-in-a-box https://mailinabox.email/ implementation.

# What does it do?

Basically, it encrypts all mail received (body only!) with a PGP public key.

# How to use,

Well, if you read the blog post, you figured it out.  I am using iOS pEp app, but I also used iOS iPGmail app and mailvelope to read the mails.

# It includes:
- Modification of dovecot config
- Added "sieve's gpg" config, so we can encrypt with publickey
- example of sieve filter so user can add it to their account
