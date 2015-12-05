
donedeal = {
    "size": "medium",
    "timedelta": {
        "active": True,
        "amount": 100,
        "format": "day",
        "operator": "<"
    },
    "query": {
        "price_from": "100",
        "price_to": "700",
        "section": "cars",
        "adType": "forsale",
        "sort": "publishDate desc",
        "make": "volvo",
        "model": "s40",
        "max": 42
    }
}

mail = {
    'sender_address': 'soeme-sender@gmail.com',
    'reciever_address': ['soeme-reciever@gmail.com'],
    'subject': 'Car Hunt: DoneDeal',
    'settings': {
        'mail_server': 'smtp.gmail.com',
        'port': 587,
        'mail_user': 'user-email@gmail.com',
        'mail_passwd': 'password'
    }
}
