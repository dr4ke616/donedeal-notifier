from client import Email
from render import Render


class MailManager(object):

    def __init__(self, client=Email, render=Render):
        self.client = client
        self.render = render

    def send_mail(self, me, you, subject, data, **kwargs):
        body = self.render().execute(data=data)
        self.client(me, you, subject, body, **kwargs).send()
