from client import DoneDeal


class DoneDealManager(object):

    def __init__(self, client=DoneDeal):
        self.client = client


class QueryManager(DoneDealManager):

    def find(self, query):
        pass


class QueryImageManager(DoneDealManager):

    def pull_images_from_query(self, query):
        pass

    def download_images_from_query(self, query):
        pass
