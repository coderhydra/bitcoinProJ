import pyupbit
import time


def mon():
    if len(str((time.localtime().tm_mon))) == 1:
        return "0" + str(time.localtime().tm_mon)
    else:
        return str(time.localtime().tm_mon)


def day():
    if len(str((time.localtime().tm_mday))) == 1:
        return "0" + str(time.localtime().tm_mday)
    else:
        return str(time.localtime().tm_mday)


class now:

    def __str__(self):
        return f'{time.localtime().tm_year}-{mon()}-{day()} {time.localtime().tm_hour}:{time.localtime().tm_min}'


def key_ticker():
    input_ticker = input("kind: 1_BTC, 2_ETH 3_SOL")
    if input_ticker == "":
        print("default: KRW-BTC")
        return 'KRW-BTC'
    elif input_ticker == "1":
        return 'KRW-BTC'
    elif input_ticker == "2":
        return 'KRW-ETH'
    elif input_ticker == "3":
        return "KRW-SOL"


def key_interval():
    input_interval = input(
        "interval: 1_minute1, 2_minute3, 3_minute5, 4_minute10, 5_minute15, 6_minute30, 7_minute60, 8_minute240, "
        "9_day, 10_week, 11_month")
    if input_interval == "":
        print("default: minute1")
        return "minute1"
    elif input_interval == "1":
        return "minute1"
    elif input_interval == "2":
        return "minute3"
    elif input_interval == "3":
        return "minute5"
    elif input_interval == "4":
        return "minute10"
    elif input_interval == "5":
        return "minute15"
    elif input_interval == "6":
        return "minute30"
    elif input_interval == "7":
        return "minute60"
    elif input_interval == "8":
        return "minute240"
    elif input_interval == "9":
        return "day"
    elif input_interval == "10":
        return "week"
    elif input_interval == "11":
        return "month"


def key_to():
    input_to = input("to: ex_2022-04-04 17:27")
    if input_to == "":
        print("default: {}".format(now()))
        return now()
    else:
        return input_to


def key_count():
    cnt = input("count: #")
    if cnt != '':
        return int(cnt)
    else:
        print("default: 100")
        return 100


class quote:
    def __init__(self, ticker, itv, to, cnt):
        self.ticker = ticker
        self.itv = itv
        self.to = to
        self.cnt = cnt

    def get_quote(self):
        return pyupbit.get_ohlcv(ticker=self.ticker, interval=self.itv, to=self.to, count=self.cnt)


def quote_now(kind):
    return pyupbit.get_current_price([kind])


def get_coin_quote():
    return quote(key_ticker(),key_interval(),str(now()),key_count()).get_quote()