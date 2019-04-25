from sys import argv
import sys
from urllib.request import urlopen
from smtplib import SMTP
import re
import time
import sched
import threading



html = urlopen("http://www.google.com/")
#print(html.read())

def main():
    if len(sys.argv) > 1:
        site_url = argv[1]
    else:
        print("first argv must be website url")
        exit
    
    if len(sys.argv) > 2:
        check_interval = int(argv[2])
    else:
        print("second argv must be time interval")
        exit

    print(html)
    #print(html.read())

if __name__ == '__main__':
    main()