# Notifier

Python app to notify you via email of latest items sold on donedeal



### Install
Make sure you have installed `libffi-dev` and `libssl-dev`. On Ubuntu machines run:
```bash
apt-get install libffi-dev libssl-dev
```

Clone and install the requirements
```bash
$ git clone https://github.com/dr4ke616/notifier
$ pip install -r requirements.txt
```

### To Run
```bash
$ python notifier/app.py
```

### Config
The config contains the query you want to run on DoneDeal and the settings for your email account. The timedelta for the time to query and format is a little wierd and hacky. DoneDeal's API doesnt seem to allow you to query for percise times (or at least I havent found a way as there is no documentatio for it). `timedelta_amount` must be a number between 1 and N and `timedelta_format`can only be either `day` or `hour`
