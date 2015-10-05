import json
import requests


class DoneDealException(Exception):
    pass


class DoneDeal(object):

    host = 'https://donedeal.ie'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    def __init__(self, host=None, headers=None):

        if host:
            self.host = host

        if headers:
            self.headers = headers

    def find(self, data):
        """ Search donedeal using following params:
            :param data: `dict` containging the key value pairs of:
            {
                section: "all"
                adType: "forsale"
                source: ''
                sort: 'relevance desc'
                area: []
                max: 30, // must be a common denominator for balanced
                    2 or 3-column layout (eg 6|12|18|24|30) etc
                start: 0
            }
        """
        uri = '{host}/search/api/v3/find/'.format(host=self.host)
        resp = requests.post(uri, data=json.dumps(data), headers=self.headers)
        if resp.status_code != 200:
            raise DoneDealException(
                'Got invalid response code of {}'.format(resp.status_code)
            )

        return resp.json()
