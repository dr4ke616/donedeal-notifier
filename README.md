# DoneDeal Notifier

Quick & dirty Python app to query and notify you via email of items sold on DoneDeal.


## Install
Make sure you have installed `libffi-dev` and `libssl-dev`. On Ubuntu machines run:
```bash
apt-get install libffi-dev libssl-dev
```

Clone and install the requirements
```bash
$ git clone https://github.com/dr4ke616/donedeal-notifier
$ pip install -r requirements.txt
```

## To Run
```bash
$ python notifier/app.py
```

## Config
The config (`notifier/config.py`) contains the query you want to run on DoneDeal and the settings for your email account.

### Size
The image size you want. One of `small`, `medium`, or `large`

### Timedelta
This is a hacky time based query. DoneDeal's API doesn't seem to allow you to query for precise times (or at least I haven't found a way as there is no documentation for it). If you want to disable this, just set `active` to `False`. The `amount` is number between `1` and `N` where the number can represent either days or hours. This representation is expressed with the `format` type. The `opertor` is the comparison operator you want to use, can be one of `==`, `>=`, `<=`, `>`, `<`. For example:
```python
"timedelta": {
    "active": True,
    "amount": 1,
    "format": "day",
    "operator": "=="
},
```

### Sample Queries:
Search for newest ads with a maximum result of 42 containing Volvo S40s between 100 and 700 Euro
```python
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
```

Search for newest ads with a maximum result of 42, containing the word "trek" in the Bicycles section
```python
{
    "sort": "publishDate desc",
    "adType": "forsale",
    "section": "bicycles",
    "words": "trek",
    "max": 42
}
```

Note: The `max` value needs to be a multiple of three to take affect. This was probably Donedeals' way to handle the grid view they use on their site.
