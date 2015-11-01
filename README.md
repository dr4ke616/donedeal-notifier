# DoneDeal Notifier

Quick & dirty Python app to notify you via email of latest items sold on DoneDeal.


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
The config (`notifier/config.py`) contains the query you want to run on DoneDeal and the settings for your email account. The timedelta for the time to query and format is a little wierd and hacky. DoneDeal's API doesnt seem to allow you to query for percise times (or at least I havent found a way as there is no documentation for it).
- timedelta_amount: A number between `1` and `N` is the number of days/hours to query for
- timedelta_format: Can only be either `day` or `hour`
- size: The image size you want. One of `small`, `medium`, or `large`
- query: Is broken into `words`, `section`, `adType`, `sort`, and `max`. Look at [DoneDeal](https://www.donedeal.ie) for more information on this.
