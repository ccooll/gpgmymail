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

# Notes and Instructions

## Disclaimer ;)

First, this is a very dirty hack.  It works and I basically just stopped there.  I decided to leave my notes on Github, but if it works, just consider
yourself lucky...  Everything here probably contains mistake...  

** Before anything, you have to install mail-in-a-box (Miab) on your system. **

## Instructions, well, kindda...

1. Get this repo or the code in here...
2. If it does not exist, create the folder /usr/lib/dovecot/sieve-filter and it should be:
> drwxr-xr-x  3 root root 4.0K Sep 14 12:10 sieve-filter
3. Copy the python application gpgmymail to /usr/lib/dovecot/sieve-filter
4. While you're there, create a "gnupg" folder
5. Adjust ownership to :
```
drwx------ 3 mail      mail 4.0K Sep 14 11:06 gnupg
-rwxr-xr-x 1 user-data root 3.8K Aug  7  2020 gpgmymail
``` 
   - We will come back here later, we will need to copy a gnupg keyring here, adjust the access rights.  Everything will need to be owned by mail:mail or gpg will complain
6. Adjust the config of Dovecot
   - Edit /etc/dovecot/conf.d/90-sieve.conf  Here is what I have :
```
plugin {
  sieve = file:~/sieve;active=~/.dovecot.sieve
  sieve_extensions = +vnd.dovecot.filter
  sieve_plugins = sieve_extprograms
}
```
   - Edit /etc/dovecot/conf.d/90-sieve-extprograms.conf  Here is what I have:
```
plugin {
  sieve_filter_socket_dir = sieve-filter
  sieve_filter_bin_dir = /usr/lib/dovecot/sieve-filter
}
```

