#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
import csv
import io
import os
import signal
import subprocess
import threading
import json
import time
import hashlib
import random 

class PerfEventsCSVDialect(csv.Dialect):
    delimiter = ' '
    lineterminator = '\n'
    quoting = csv.QUOTE_NONE
    skipinitialspace = True

class Stats(threading.Thread):
    def __init__(self, timeout, filename):
        self._timeout = timeout
        self._fname = filename
        self._json_file = '/tmp/' + hashlib.md5(str(random.random()).encode()).hexdigest() + ".json"
        self._open_file()
        threading.Thread.__init__(self)
    
    def _open_file(self):
        self._f = open(self._json_file, "w")

    def run(self):
        try:
            cmd = ["mpstat", "1", f"{self._timeout + 1}",
                   "-o", "JSON"]
            self.process = subprocess.Popen(cmd, universal_newlines=True,
                                            stdout=self._f,
                                            stderr=subprocess.DEVNULL)
            self.process.wait()
        except subprocess.CalledProcessError as e:
            log.error(f"Error collecting performance events: {e}")

    def stop(self):
        try:
            # sleep for 2 cycles for mpstat to cool down
            time.sleep(2)
            # Grep process id of sleep
            cmd = ["pgrep", "-P", f"{self.process.pid}"]
            run = subprocess.run(cmd,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.DEVNULL)
            pid_str = run.stdout.strip().decode('utf-8')
            if pid_str == "":
                pid = -1
            else:
                pid = int(pid_str)

            if pid:
                os.kill(pid, signal.SIGTERM)
                os.kill(pid, signal.SIGKILL)
        except subprocess.CalledProcessError as e:
            log.error(f"Error stopping performance event mpstat 1 timeout: {e}")

        self.process.wait()
        if self._f.closed <= 0:
            self._f.close()
        return self.parse()

    def parse(self):
        # Parse performance data
        try:
            f = open(self._json_file, "r")
            #print(f.read())
            read_data = f.read()
            data = json.loads(read_data)
        except json.JSONDecodeError as je:
            read_data += ']}]}}'
            data = json.loads(read_data)
        except Exception as e:
            print("Error:", e)
            #f.close()
            return -1
        
        if f.closed <= 0:
            f.close()
        
        cpu_usr = []
        cpu_sys = []
        cpu_iowait = []
        for readings in data["sysstat"]["hosts"][0]["statistics"]:
            cpu_usr.append(readings["cpu-load"][0]["usr"])
            cpu_sys.append(readings["cpu-load"][0]["sys"])
            cpu_iowait.append(readings["cpu-load"][0]["iowait"])
        
        readings_dict = {}
        readings_dict['usr'] = cpu_usr
        readings_dict['sys'] = cpu_sys
        readings_dict['iowait'] = cpu_iowait
                
        return readings_dict
