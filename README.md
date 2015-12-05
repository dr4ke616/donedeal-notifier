# DoneDeal Notifier

Quick & dirty Python app to query and notify you via email of items sold on DoneDeal.


### Install
Make sure you have installed `libffi-dev` and `libssl-dev`. On Ubuntu machines run:
```bash
apt-get install libffi-dev libssl-dev
```

Clone and install the requirements
```bash
$ git clone https://github.com/dr4ke616/donedeal-notifier
$ pip install -r requirements.txt
```

### To Run
```bash
$ python notifier/app.py
```

### Config
The config (`notifier/config.py`) contains the query you want to run on DoneDeal and the settings for your email account. The timedelta for the time to query and format is a little weird and hacky. DoneDeal's API doesn't seem to allow you to query for precise times (or at least I haven't found a way as there is no documentation for it).
- *timedelta_amount*: A number between `1` and `N` is the number of days/hours to query for
- *timedelta_format*: Can only be either `day` or `hour`
- *size*: The image size you want. One of `small`, `medium`, or `large`
- *query*: See below for examples.

### Sample Queries:
Search for newest ads with a maximum result of 42 containing Volvo S40s between 100 and 700 Euro
```json
{
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
```json
{
    "sort": "publishDate desc",
    "adType": "forsale",
    "section": "bicycles",
    "words": "trek",
    "max": 42
}
```

Note: The `max` value needs to be a multiple of three to take affect. This was probably Donedeals' way to handle the grid view they use on their site.
