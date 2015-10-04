import smtplib

from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class Email(object):

    mail_server = 'localhost'
    port = 0
    mail_user = None
    mail_passwd = None

    def __init__(self, me, you, subject, body, **kwargs):
        self.me = me
        self.you = you
        self.subject = subject
        self.body = body

        for key, value in kwargs.items():
            setattr(self, key, value)

        self._build_mime_multipart()

    def __str__(self):
        return self._message.as_string()

    def _build_mime_multipart(self):
        mime = MIMEMultipart('alternative')
        mime['Subject'] = self.subject
        mime['From'] = self.me
        mime['To'] = self.you
        mime.attach(MIMEText(self.body, 'plain'))
        self._message = mime

    def _authenticate(self, smtpserver):
        if self.mail_user is not None or self.mail_passwd is not None:
            smtpserver.ehlo()
            smtpserver.starttls()
            # smtpserver.ehlo
            smtpserver.login(self.mail_user, self.mail_passwd)

    def attach(self, attachment):
        with open(attachment, "rb") as f:
            self._message.attach(MIMEApplication(
                f.read(),
                Content_Disposition='attachment; filename="%s"' % basename(f),
                Name=basename(f)
            ))

    def send(self):

        smtpserver = smtplib.SMTP(self.mail_server, self.port)
        self._authenticate(smtpserver)

        smtpserver.sendmail(self.me, self.you, str(self))
        smtpserver.close()


if __name__ == '__main__':
    Email(
        'adamdrakeford@gmail.com',
        'adamdrakeford@gmail.com',
        'Test',
        'This is a test'
    ).send()
