#! /usr/bin/env python
import psutil
import argparse
import json
import schedule
import time
from datetime import datetime
n = 0
f = open('test.json', 'w')
f.close
f = open('test.txt', 'w')
f.close
parser = argparse.ArgumentParser()
parser.add_argument(
    "-i", help="Interval between snapshots in seconds", type=int, default=30)
parser.add_argument("-t", help="Output file type", default="txt")
args = parser.parse_args()


class Monitor:
    name = "My Monitor"
    cpu_usage = "cpu_percent"
    memory_used = "memory"
    percent_mem = "memory percent"

    def __repr__(self):
        return " % s cpu_usage:% s memory_used:% s percent_mem:% s" % (
            self.name, self.cpu_usage, self.memory_used, self.percent_mem)


def job():
    global n
    global args
    n += 1
    snapshot = Monitor()
    now = datetime.now()
    name = 'SNAPSHOT ' + str(n) + ":" + str(now)
    snapshot.name = name
    snapshot.cpu_usage = psutil.cpu_percent(interval=2)
    snapshot.memory_used = psutil.virtual_memory().total >> 20
    snapshot.percent_mem = psutil.virtual_memory().percent
    if args.t == "json":
        jsonStr = json.dumps(snapshot.__dict__, indent=2)
        f = open('test.json', 'a')
        print(jsonStr, file=f)
        f.close
        print(jsonStr)
    else:
        f = open('test.txt', 'a')
        print(snapshot, file=f)
        f.close
        print(snapshot)

def main():
    job()
    schedule.every(args.i).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)