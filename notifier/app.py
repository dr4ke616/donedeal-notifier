import os
import sys
import config

if 'notifier' not in sys.path:
    sys.path.append(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), '../'))

from notifier.mail.manager import MailManager  # noqa
from notifier.donedeal.manager import QueryImageManager  # noqa


def main():
    response = QueryImageManager().pull_images_from_query(
        config.donedeal['timedelta_amount'],
        config.donedeal['timedelta_format'],
        config.donedeal['size'],
        **config.donedeal['query']
    )

    MailManager().send_mail(
        config.mail['sender_address'],
        config.mail['reciever_address'],
        config.mail['subject'],
        response
    )


if __name__ == '__main__':
    main()
