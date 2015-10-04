

class DoneDeal(object):

    def __init__(self):
        pass

    def find(self, query):
        """ Search donedeal using following params:
            section: "all"
            adType: "forsale"
            source: ''
            sort: 'relevance desc'
            area: []
            max: 30, // must be a common denominator for balanced 2 or 3-column
                layout (eg 6|12|18|24|30) etc
            start: 0
            :param query: `dict` containging the key value pairs of the above
                    data

            TODO: query with following
                {
                    "words": "trek",
                    "section": "bicycles",
                    "adType": "forsale",
                    "sort": "publishDate desc",
                    "max": 42
                }
        """
