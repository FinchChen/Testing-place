import time


a = "22:24:24 2016"
b = "2017-11-11 12:12:12"
print time.mktime(time.strptime(a,"%H:%M:%S %Y"))
print time.mktime(time.strptime(b,"%Y-%m-%d %H:%M:%S"))