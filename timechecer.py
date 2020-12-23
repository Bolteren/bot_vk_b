import datetime
import sqlfunction


def seconds_to_dhms(seconds):
    days = seconds // (3600 * 24)
    hours = (seconds // 3600) % 24
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    return days, hours, minutes, seconds


class checker:
    def __init__(self):
        self.nowtime = datetime.datetime.now().time()
        self.last_cheack = (datetime.datetime.now() - datetime.timedelta(minutes=1)).time()

    def cheack(self):
        if self.nowtime > self.last_cheack:
            db = sqlfunction.msql()
            t = db.select_time()
            result = list()
            if t:
                for r in t:
                    tmp = str(r[0]).split(':')
                    if int(tmp[0]) * 60 + int(tmp[1]) <= (self.nowtime.hour * 60 + self.nowtime.minute):
                        db.update_none(id_user=int(r[1]))
                        res = {'user': r[1], 'time': r[0]}
                        result.append(res)
            return result


def main():
    dt = checker()
    responce = dt.cheack()
    for r in responce:
        print(r['user'], ' - ', r['time'])


if __name__ == "__main__":
    main()
