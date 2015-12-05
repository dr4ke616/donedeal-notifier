from client import DoneDeal
from timedelta import TimeDelta


class DoneDealManager(object):

    client = DoneDeal()

    def __init__(self, client=None):
        if client:
            self.client = client


class QueryManager(DoneDealManager):

    def find(self, **data):
        """ Execute a query using the client
            :param section:     "all"
            :param adType:      "forsale"
            :param source:      ''
            :param sort:        'relevance desc'
            :param area:        []
            :param max:         30, - must be a common
                denominator (eg 6|12|18|24|30)
            :param: start: 0

            TODO: query with following
                {
                    "words": "trek",
                    "section": "bicycles",
                    "adType": "forsale",
                    "sort": "publishDate desc",
                    "max": 42
                }
        """
        return self.client.find(data)


class QueryImageManager(QueryManager):

    def pull_images_from_query(self, size, timedelta, **data):
        """ Pull all image urls from response
            :param size: The size of the image. Can either
                be small, medium or large
            :param td_amount: The timedelta to include. DoneDeal
                doesnt seem to allow you to query for percise
                times, so we are doing it the quick and dirty way.
                This param must be a number between 1 and N
            :param td_format: The format to use. Either day or
                hour
        """
        if size not in ('small', 'medium', 'large'):
            raise ValueError(
                'You need to specify either small, '
                'medium or large for image size'
            )

        content = self.find(**data)['ads']

        if timedelta['active']:
            print('TimeDelta active.')
            content = TimeDelta(
                timedelta['amount'],
                timedelta['format'],
                timedelta['operator']
            ).parse(content)

        return [
            (con['header'], con['age'], con['description'], con['friendlyUrl'],
                [photo[size] for photo
                    in con.get('photos', [])]) for con in content
        ]
