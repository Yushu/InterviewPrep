import requests,os
import mysql.connector
import pandas as pd

a = {}
b = {}
for r, d, com_err in os.walk('/root/devops/'):
    for f in com_err:
        t = r + "/" + f
        if f not in a:
            a[f] = []
        a[f] += [open(t).read()]
cnt_err = 0
for i in a:
    if i.split(".")[1] == 'log':
        for j in a[i][0].split("\n"):
            x = j.split("|")
            if len(x) > 2 and x[1] == 'ERROR':
                if x[2] in b:
                    b[x[2]] += 1
                else:
                    b[x[2]] = 1
        cnt_err += 1
for i in sorted(set(b.values()), reverse=True):
    for j in sorted(b.keys()):
        if b[j] == i:
            print(j + ' ' + str(i))