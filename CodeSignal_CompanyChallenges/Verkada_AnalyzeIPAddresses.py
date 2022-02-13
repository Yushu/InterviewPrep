import requests
import mysql.connector
import pandas as pd
import os
from functools import reduce
import re

def findIP(root_dir):
    pattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    possible_ips = set()
    for path, directory, filenames in os.walk(root_dir):
        for filename in filenames:
            with open(f"{path}/{filename}", "rt") as f:
                possible_ips.update(set(re.findall(pattern, f.read())))
    return possible_ips

def validateIP(ip):
    is_valid = True
    splited_ip = ip.split('.')
    for element in splited_ip:
        element = int(element)
        if element > 255 or element < 0:
            is_valid = False
            break
    return is_valid

possible_ips = findIP('/root/data')
valid_ips = [ip for ip in possible_ips if validateIP(ip)]
for ip in sorted(set(valid_ips)):
    print(ip)