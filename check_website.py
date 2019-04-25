from sys import argv
import sys
import requests
from urllib.request import urlopen
from smtplib import SMTP
import re
import time
import sched
import threading



html = urlopen("http://www.google.com/")
#print(html.read())

# Checks that correct arguments are present and shows
# correct usage if error occurs
def check_argvs():
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

# Checks that user has connection, checks google and yahoo
# because its not likely that both are down lol
def check_connection():
    g = requests.get('http://google.com')
    y = requests.get('http://yahoo.com')
    if g and y:
        print ("internet is connected")
        return True
    if not g and not y:
        print ("internet down")
        return False

# Checks website connection of user's choice
def check_url(url):
    if check_connection():
        url_check = requests.get(url)
        if url_check:
            print (url + " is online!!")
        else:
            print ("%s is down!!" % url)
    else:
        print ("internet connection is down")

def main():
    check_argvs()
    #check_connection()
    site_url = argv[1]
    print("url is " + site_url)
    check_url(site_url)
    print(html)
    #print(html.read())

if __name__ == '__main__':
    main()