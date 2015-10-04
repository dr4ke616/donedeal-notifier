from client import Email


class MailManager(object):

    def __init__(self, client=Email):
        self.client = client
