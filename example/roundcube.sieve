require ["fileinto", "vnd.dovecot.filter"];
# rule:[All]
if true
{
	filter "gpgmymail" "USER@DOMAIN.com";
  	fileinto "INBOX";
}
