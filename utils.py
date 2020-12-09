import time
import datetime


def unix_timestamp() -> int:
    return int(time.time())


def readable_time(timestamp) -> str:
    return str(time.strftime("%b-%d-%Y %H:%M:%S", datetime.datetime.fromtimestamp(timestamp).timetuple()))