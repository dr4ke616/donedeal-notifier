

TIME_FORMAT = ('day', 'hour')
OPERATORS = {
    '==': lambda x, y: x == y,
    '<=': lambda x, y: x <= y,
    '>=': lambda x, y: x >= y,
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
}


class TimeDelta(object):

    def __init__(self, amount, fmt, operator):
        if int(amount) < 0:
            raise ValueError('amount must be over zero')

        if fmt not in TIME_FORMAT:
            raise ValueError(
                'Time format must be one of {}'
                ''.format(', '.join(TIME_FORMAT))
            )

        if operator not in OPERATORS.keys():
            raise ValueError(
                'Comparision type must be one of {}'
                ''.format(', '.join(OPERATORS.keys()))
            )

        if int(amount) > 1:
            fmt += 's'

        self.amount = amount
        self.format = fmt
        self.operator = operator

    def parse(self, results):
        d = []
        for content in results:
            # O(N) - hacky as fuck! :(
            val, fmt = content['age'].split(' ')
            if fmt == self.format and \
                    OPERATORS[self.operator](int(val), int(self.amount)):
                d.append(content)
        return d
